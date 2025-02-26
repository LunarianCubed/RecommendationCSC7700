import sys
# from get_movie import get_movie
from model import train_svd
from data_loader import load_data, get_movie_info
from recommend import create_matrix, recommend_movies, get_movie_info


def main(*args):
    args = sys.argv
    user_id = null

    if "-u" in  args:
        user_id = args[args.index("-u") + 1]

    if user_id == null:
        user_id = input("Enter the user_id you want to recommend to:")

    df, movie_info= load_data()

    user_factors, movie_factors = train_svd(rating_matrix)
    predicted_ratings = np.dot(user.factors, movie_factors)

    recommend_movies(user_id)


if __name__ == "__main__":
    main()
