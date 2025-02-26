import requests
import configparsar
import pandas as pd

movie_df = pd.read_csv("./ml-32m/movies.csv")
movie_info = dict(zip(movies_df["movieId"], zip(movie_df["title"], movies_df["genres"])))


# config = configparsar.configparsar()
# config.read('config.ini')
# api_key = config['DEFAULT']['OMDb_api']
# url = f'http://www.omdbapi.com/?apikey={api_key}''


