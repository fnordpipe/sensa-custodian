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
    self.data['summary'] = []
    self.data['releases'] = []
    self.data['description'] = []
    self.data['solution'] = []
    self.data['bugs'] = []
    self.data['packages'] = []
    self.data['references'] = []
    _releases = []
    topic = None

    for line in lines:
      # find beginning of text block
      if line.endswith(b'Summary:'):
        topic = 'summary'
        continue
      if line.endswith(b'Relevant releases/architectures:'):
        topic = 'releases'
        continue
      if line.endswith(b'Description:'):
        topic = 'description'
        continue
      if line.endswith(b'Solution:'):
        topic = 'solution'
        continue
      if line.endswith(b'Bugs fixed (https://bugzilla.redhat.com/):'):
        topic = 'bugs'
        continue
      if line.endswith(b'Package List:'):
        topic = 'packages'
        continue
      if line.endswith(b'References:'):
        topic = 'references'
        continue
      if line.endswith(b'Contact:'):
        topic = 'contact'
        continue

      if topic in ['summary', 'description', 'solution']:
        self.data[topic].append(line)

      if topic in ['bugs', 'references'] and line:
        if topic == 'bugs':
          self.data[topic].append(line.split(b' - '))
        else:
          self.data[topic].append(line)

      if topic == 'releases' and line:
        release = line.split(b' - ')
        release[1] = release[1].split(b', ')
        _releases.append(release[0])
        self.data[topic].append(release)

      if topic == 'packages':
        if line.strip(b':') in _releases:
          self.data[topic].append([line.strip(b':')])
        elif line.endswith(b':'):
          arch = line.strip(b':')
          if arch == 'Source':
            arch = arch.lower()
          self.data[topic][-1].append([arch, []])
        elif line.endswith(b'.rpm'):
          self.data[topic][-1][-1][1].append(line)

    for t in ['description', 'solution', 'summary']:
      if not self.data[t][0] and not self.data[t][-1]:
        self.data[t] = b'\n'.join(self.data[t][1:-1])

    return self.data
