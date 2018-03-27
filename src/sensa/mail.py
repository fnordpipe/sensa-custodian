#!/usr/bin/env python

from sensa.rhsa import SensaRHSAParser

PROVIDER = {
  'rhsa': 'rhsa-announce@redhat.com'
}

class SensaMail(object):
  def __init__(self, raw, provider):
    self.raw = raw
    self.provider = provider

    self.parse()

  def parse(self):
    if self.provider == 'rhsa':
      parser = SensaRHSAParser()

    if parser:
      self.data = parser.parse(self.raw)
