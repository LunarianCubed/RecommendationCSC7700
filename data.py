import requests
import configparsar

config = configparsar.configparsar()
config.read('config.ini')
api_key = config['DEFAULT']['api_key']
