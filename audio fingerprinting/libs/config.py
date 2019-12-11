import json
import os.path

CONFIG_DEFAULT_FILE = 'config.json'
CONFIG_DEVELOPMENT_FILE = 'config-development.json'

def get_config():
  defaultConfig = {"env": "unknown"}

  return merge_configs(
    defaultConfig,
    parse_config(CONFIG_DEFAULT_FILE),
    parse_config(CONFIG_DEVELOPMENT_FILE)
  )
def parse_config(filename):
  config = {}

  if os.path.isfile(filename):
    f = open(filename, 'r')
    config = json.load(f)
    f.close()

  return config
def merge_configs(*configs):
  z = {}

  for config in configs:
    z.update(config)

  return z
