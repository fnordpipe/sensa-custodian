#!/usr/bin/env python

import datetime
import psycopg2

class SensaMigrate(object):
  def __init__(self, config):
    self.config = config
    self.init_db()
    self.init_migration()

  def init_db(self):
    self.db = psycopg2.connect(
      host = self.config['db']['host'],
      port = self.config['db']['port'],
      user = self.config['db']['user'],
      password = self.config['db']['pass'],
      dbname = self.config['db']['name']
    )

  def init_migration(self):
    def create_tables():
      cursor = self.db.cursor()
      cursor.execute(
        "CREATE TABLE IF NOT EXISTS advisory ( \
            id SERIAL PRIMARY KEY NOT NULL, \
            advisory VARCHAR(20) UNIQUE NOT NULL, \
            subject VARCHAR(255) NOT NULL, \
            severity VARCHAR(10) NOT NULL, \
            url VARCHAR(255) NOT NULL, \
            product TEXT NOT NULL, \
            description TEXT NOT NULL, \
            summary TEXT NOT NULL, \
            solution TEXT );")

      cursor.execute(
        "CREATE TABLE IF NOT EXISTS bug ( \
            id SERIAL PRIMARY KEY NOT NULL, \
            advisory_id INT NOT NULL, \
            issue INT NOT NULL, \
            summary VARCHAR(255) NOT NULL );")

      cursor.execute(
        "CREATE TABLE IF NOT EXISTS cve ( \
            id SERIAL PRIMARY KEY NOT NULL, \
            advisory_id INT NOT NULL, \
            cve VARCHAR(20) NOT NULL );")

      cursor.execute(
        "CREATE TABLE IF NOT EXISTS reference ( \
            id SERIAL PRIMARY KEY NOT NULL, \
            advisory_id INT NOT NULL, \
            reference VARCHAR(255) NOT NULL );")

      cursor.execute(
        "CREATE TABLE IF NOT EXISTS release ( \
            id SERIAL PRIMARY KEY NOT NULL, \
            release TEXT NOT NULL);")

      cursor.execute(
        "CREATE TABLE IF NOT EXISTS architecture ( \
            id SERIAL PRIMARY KEY NOT NULL, \
            architecture VARCHAR(10) NOT NULL );")

      cursor.execute(
        "CREATE TABLE IF NOT EXISTS package ( \
            id SERIAL PRIMARY KEY NOT NULL, \
            package VARCHAR(255) NOT NULL );")

      cursor.execute(
        "CREATE TABLE IF NOT EXISTS advisory_release_architecture ( \
            id SERIAL PRIMARY KEY NOT NULL, \
            advisory_id INT NOT NULL, \
            release_id INT NOT NULL, \
            architecture_id INT NOT NULL, \
            package_id INT NOT NULL );")

    self.migration = {
      1: create_tables
    }

  def run(self):
    print('start migrations...')
    cursor = self.db.cursor()
    cursor.execute(
      "CREATE TABLE IF NOT EXISTS migrations ( \
        version INT PRIMARY KEY NOT NULL, \
        date TIMESTAMP NOT NULL );")

    for k, v in self.migration.items():
      m = cursor.execute("SELECT version FROM migrations WHERE version = %s;", [k])
      if not m:
        v()
        cursor.execute("INSERT INTO migrations (version, date) VALUES (%s, %s);", (k, datetime.datetime.utcnow().isoformat()))
        print('[%s]: migrated' % k)

    if cursor:
      cursor.close()
    self.db.commit()
    self.db.close()
