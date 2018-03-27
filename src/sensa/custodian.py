#!/usr/bin/env python

import email.utils
import psycopg2
from smtpd import SMTPServer

from sensa.mail import PROVIDER
from sensa.mail import SensaMail

class SensaCustodian(SMTPServer):
  def __init__(self, config):
    self.config = config
    self.init_whitelist_from()
    self.init_db()
    super(SensaCustodian, self).__init__(
      ('0.0.0.0', self.config['smtp']['port']),
      None)

  def __del__(self):
    if hasattr(self, 'db'):
      self.db.close()

  def init_db(self):
    self.db = psycopg2.connect(
      "host='%s' port='%s' user='%s' password='%s' dbname='%s'" % (
      self.config['db']['host'],
      self.config['db']['port'],
      self.config['db']['user'],
      self.config['db']['pass'],
      self.config['db']['name']
    ))

  def init_whitelist_from(self):
    self.whitelist_from = []
    for s in self.config['subscriptions']:
      self.whitelist_from.extend([PROVIDER[s]])

  def parse_address(self, address):
    sender = email.utils.parseaddr(address)
    provider = None

    for k, v in PROVIDER.items():
      if v == sender[1]:
        provider = k

    return {
      'name': sender[0],
      'address': sender[1],
      'provider': provider
    }

  def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
    sender = self.parse_address(mailfrom.strip('"'))

    if sender['address'] in self.whitelist_from:
      sensa_mail = SensaMail(data, sender['provider'])
