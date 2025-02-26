import pandas as pd

def load_data(df_path="./ml-32m/ratings.csv", movie_df_path="./ml-32m/movies.csv"):
    df = pd.read_csv(df_path, dtype={'userId': 'int32', 'movieId': 'int32', 'rating': 'float32'})
    movie_df = pd.read_csv(movie_df_path)
    movie_info = dict(zip(movie_df["movieId"], zip(movie_df["title"], movie_df["genres"])))

    #for testing
    #df = pd.read_csv(df_path, dtype={'userId': 'int32', 'movieId': 'int32', 'rating': 'float32'}, nrows=1000)

    return df, movie_info

def get_movie_info(movies, movie_info):
    formatted_movies=[]
    for movie_Id in movies:
        if movie_Id in movie_info:
            title, genres = movie_info[movie_Id]
            formatted_movies.append(f"{title.ljust(28)} {genres}")
    return formatted_movies

if __name__ == "__main__":
    df, movie_df = load_data()
    print(df.head())
