#!/usr/bin/env python

"""USAGE: sensa-custodian.py [-c FILE]

errata / security advisory smtp/imap listener

-c FILE   specify config file [default: /etc/sensa/custodian.conf]

"""

import asyncore
import docopt
import json
import os.path
import psycopg2
import sys

from sensa.custodian import SensaCustodian

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

    try:
      sensa = SensaCustodian(config)
    except psycopg2.OperationalError:
      print('Cannot connect to database')
      sys.exit(1)

    asyncore.loop()
  else:
    print('No such file: %s' % config_file)
    sys.exit(1)

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt as e:
    print('\nInterrupted by User')
