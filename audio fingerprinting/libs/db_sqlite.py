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

