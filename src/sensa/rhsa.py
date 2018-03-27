#!/usr/bin/env python

class SensaRHSAParser(object):
  def __init__(self):
    self.data = {}

  def parse(self, raw):
    for line in raw.splitlines():
      # read subject
      if line.startswith(b'Subject:') and 'subject' not in self.data:
        self.data['subject'] = line.replace(b'Subject:', b'').strip()

    print(self.data['subject'])
