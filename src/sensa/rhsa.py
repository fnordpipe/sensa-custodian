#!/usr/bin/env python

class SensaRHSAParser(object):
  def __init__(self):
    self.data = {}

  def parse(self, raw):
    _synopsis = None
    _lines = 0
    _metadata = 0
    lines = raw.splitlines()

    for line in lines:
      _lines += 1

      # read subject
      if line.startswith(b'Subject:') and 'subject' not in self.data:
        subject = line.replace(b'Subject:', b'').strip()
        self.data['id'] = subject[subject.find(b'[')+1:subject.find(b']')]
        self.data['severity'] = subject[len(self.data['id'])+2:subject.rfind(b':')].strip()
        self.data['subject'] = subject[subject.rfind(b':')+2:]

      # verify synopsis
      if line.startswith(b'Synopsis:') and not _synopsis:
        synopsis = line.replace(b'Synopsis:', b'').strip().split(b':')
        if self.data['severity'] == synopsis[0] and self.data['subject'] == synopsis[1].strip():
          _synopsis = True
        else:
          self.data = {}
          return None

      # read product
      if line.startswith(b'Product:'):
        self.data['product'] = line.replace(b'Product:', b'').strip()

      # read advisory url
      if line.startswith(b'Advisory URL:'):
        self.data['advisory-url'] = line.replace(b'Advisory URL:', b'').strip()

      # read cve names
      if line.startswith(b'CVE Names:'):
        self.data['cve'] = line.replace(b'CVE Names:', b'').strip().split()

      # read metadata separator
      if line.startswith(b'====') and line.endswith(b'===='):
        _metadata += 1
        if _metadata == 2:
          break

    lines = lines[_lines:]

    return self.data
