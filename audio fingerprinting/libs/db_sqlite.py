from .db import Database
from .config import get_config
import sqlite3
import sys
from itertools import zip_longest
from termcolor import colored

class SqliteDatabase(Database):
  TABLE_SONGS = 'songs'
  TABLE_FINGERPRINTS = 'fingerprints'

  def __init__(self):
    self.connect()

  def connect(self):
    config = get_config()

    self.conn = sqlite3.connect(config['db.file'])
    self.conn.text_factory = str

    self.cur = self.conn.cursor()

    print(colored('sqlite - connection opened','white',attrs=['dark']))

  def __del__(self):
    self.conn.commit()
    self.conn.close()
    print(colored('sqlite - connection has been closed','white',attrs=['dark']))

  def query(self, query, values = []):
    self.cur.execute(query, values)

  def executeOne(self, query, values = []):
    self.cur.execute(query, values)
    return self.cur.fetchone()

  def executeAll(self, query, values = []):
    self.cur.execute(query, values)
    return self.cur.fetchall()

  def buildSelectQuery(self, table, params):
    conditions = []
    values = []

    for k, v in enumerate(params):
      key = v
      value = params[v]
      conditions.append("%s = ?" % key)
      values.append(value)

    conditions = ' AND '.join(conditions)
    query = "SELECT * FROM %s WHERE %s" % (table, conditions)

    return {
      "query": query,
      "values": values
    }

 