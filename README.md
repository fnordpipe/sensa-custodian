# sensa; easy (and) neat security advisories

I wrote this tool to get a better overview about existing security issues regarding the software
that is in place.
Most software distributors are sending their security advisories via mail therefore
**sensa** is listening to these mails and normalizes it for persistence.

## requirements

* postfix
* a postgres database
* python-asyncore
* python-docopt
* python-json
* python-psycopg2

> instead of postfix you can use any other MTA that is able to redirect messages
> from security-advisory mailing-lists to another relay.

## usage

    $ sensa-custodian.py [-c FILE]

the default config file is located at `/etc/sensa/custodian.conf`

    $ cat custodian.conf
    {
      "db": {
        "host": "127.0.0.1",
        "port": "5432",
        "user": "sensa",
        "pass": "changeme",
        "name": "sensa"
      },
      "smtp": {
        "port": 10025
      },
      "subscriptions": [
        "rhsa"
      ]
    }
