import pandas as pd
import numpy as np
from sklearn.decomposition import TruncatedSVD

df = pc.read_csv("./ml-32m/ratings.csv")
rating_matrix = df.pivot(index="userID", columns="movieID", value="rating").fillna(0)

svd = TruncatedSVD()



svd = TruncatedSVD(n_components=2)
user_factors = svd.fit_transform(rating_matrix) 
movie_factors = svd.components_ 

predicted_ratings = np.dot(user_factors, movie_factors)

def recommend_movies(user_id, num_recommendations=3):
    if user_id not in rating_matrix.index:
        print("Invalid user ID")
        return []

    user_index = rating_matrix.index.get_loc(user_id)
    user_pred = predicted_ratings[user_index]
    already_rated = df[df["userId"] == user_id]["movieId"].tolist()
    sorted_indices = np.argsort(user_pred)[::-1]
    recommended_movies = [movie for movie in rating_matrix.columns[sorted_indices] if movie not in already_rated]
    
    return recommended_movies[:num_recommendations]
