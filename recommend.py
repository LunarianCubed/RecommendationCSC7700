import numpy as np
from sklearn.decomposition import TruncatedSVD
from data_loader import load_data

# df = pc.read_csv("./ml-32m/ratings.csv")
# movie_df = pd.read_csv("./ml-32m/movies.csv")



svd = TruncatedSVD(n_components=2)

df, _ = load_data()

def recommend_movies(user_id, rating_matrix, predicted_ratings, num_recommendations=3):
    if user_id not in rating_matrix.index:
        print("Invalid user ID")
        return []

    user_index = rating_matrix.index.get_loc(user_id)
    user_pred = predicted_ratings[user_index]

    # already_rated = df[df["userId"] == user_id]["movieId"].tolist()
    already_rated = rating_matrix.loc[user_id][rating_matrix.loc[user_id] > 0].index.tolist()
    sorted_indices = np.argsort(user_pred)[::-1]
    recommended_movies = [movie for movie in rating_matrix.columns[sorted_indices] if movie not in already_rated]
    
    return recommended_movies[:num_recommendations]


if __name__ == "__main__":
    print("usage: py main.py -u <user_id>")
