import requests
import configparsar

config = configparsar.configparsar()
config.read('config.ini')
api_key = config['DEFAULT']['OMDb_api']


url = f'http://www.omdbapi.com/?apikey={api_key}''

