import sys
import numpy as np
# from get_movie import get_movie
from model import train_svd
from data_loader import load_data, get_movie_info
from recommend import recommend_movies


def main(*args):

    print("Usage: python main.py -u <user_id> [-f]  # -f use full dataset")


    args = sys.argv
    user_id = None

    if "-u" in  args:
        try:
            user_id = int(args[args.index("-u") + 1])
        except (IndexError, ValueError):
            print("Usage: python main.py -u <user_id>")
            return

    if user_id is None:
        try:
            user_id = int(input("Enter the user_id you want to recommend to:"))
        except ValueError:
            print("Invalid user ID")
            return

    if "-f" in args:
        df, movie_info= load_data(full=True)
    else:
        df, movie_info= load_data(full=False)

    rating_matrix = df.pivot(index="userId", columns="movieId", values="rating").fillna(0)

    user_factors, movie_factors = train_svd(rating_matrix)
    predicted_ratings = np.dot(user_factors, movie_factors)

    recommended_movies_ids = recommend_movies(user_id=user_id, rating_matrix=rating_matrix, predicted_ratings=predicted_ratings)

    if recommended_movies_ids:
        print("Recommended movies:")
        formatted_movies = get_movie_info(recommended_movies_ids, movie_info)
        for movie in formatted_movies:
            print(movie)
    else:
        print("No recommendations available.")

    sys.exit(0)



if __name__ == "__main__":
    main()
