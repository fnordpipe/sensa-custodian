#!/usr/bin/env python

import email.utils
import psycopg2
from smtpd import SMTPServer

PROVIDER = {
  'rhsa': 'rhsa-announce@redhat.com'
}

class SensaCustodian(SMTPServer):
  def __init__(self, config):
    self.config = config
    self.rcpt_whitelist = self.initWhitelistFrom()
    self.initDB()
    super(SensaCustodian, self).__init__(
      ('0.0.0.0', self.config['smtp']['port']),
      None)

  def __del__(self):
    if hasattr(self, 'db'):
      self.db.close()

  def initDB(self):
    self.db = psycopg2.connect(
      "host='%s' port='%s' user='%s' password='%s' dbname='%s'" % (
      self.config['db']['host'],
      self.config['db']['port'],
      self.config['db']['user'],
      self.config['db']['pass'],
      self.config['db']['name']
    ))

  def initWhitelistFrom(self):
    self.whitelist_from = []
    for s in self.config['subscriptions']:
      self.whitelist_from.extend([PROVIDER[s]])

  def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
    if email.utils.parseaddr(mailfrom.strip('"'))[1] in self.whitelist_from:
      print('got mail')
