import numpy as np
from sklearn.decomposition import TruncatedSVD

def train_svd(rating_matrix, n_components=2):
    svd = TruncatedSVD(n_components=n_components)
    user_factors = svd.fit_transform(rating_matrix)
    movie_factors = svd.components_
    return user_factors, movie_factors
