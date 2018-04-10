#!/usr/bin/env python

"""USAGE: sensa_db_migrate.py [-c FILE]

initialize/migrate sensa database

-c FILE   specify config file [default: /etc/sensa/custodian.conf]

"""

import docopt
import json
import os.path
import sys

from sensa.db import SensaMigrate

def main():
  args = docopt.docopt(__doc__)
  config_file = args['-c']

  if os.path.isfile(config_file):
    with open(config_file, 'r') as fd:
      try:
        config = json.load(fd)
      except json.decoder.JSONDecodeError:
        print('Cannot parse config file!')
        sys.exit(1)

    SensaMigrate(config).run()
  else:
    print('No such file: %s' % config_file)
    sys.exit(1)

if __name__ == '__main__':
  main()
