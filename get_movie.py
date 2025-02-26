import requests
import configparsar
import pandas as pd

config = configparsar.configparsar()
config.read('config.ini')
api_key = config['DEFAULT']['OMDb_api']


url = f'http://www.omdbapi.com/?apikey={api_key}''

def get_movie(movie_id):
    movie_list = pc.read_csv("./ml-32m/movies.csv")
    


# movieId,title,genres
# 1,Toy Story (1995),Adventure|Animation|Children|Comedy|Fantasy
# 2,Jumanji (1995),Adventure|Children|Fantasy
