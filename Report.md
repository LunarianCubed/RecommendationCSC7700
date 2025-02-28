# **Movie Recommendation System Using SVD**

## **1. Introduction**

### **1.1 Problem Statement**

In today’s digital world, streaming platforms and online movie services generate massive amounts of content. However, users often struggle to find relevant movies that match their preferences. A recommendation system provides a solution by analyzing past interactions and predicting movies that users are likely to enjoy.

### **1.2 Motivation**

Personalized recommendations enhance the user experience, increase engagement, and optimize content discovery. Our system leverages **collaborative filtering** with **Singular Value Decomposition (SVD)** to provide accurate movie recommendations based on past user ratings.

------

## **2. Dataset and Preprocessing**

### **2.1 Data Source**

The dataset used in this project is from **MovieLens (ml-32m)**, a widely used benchmark dataset for recommendation systems. It includes:

##### ratings.csv: 

User ratings of movies with three key columns:

- `userId`: Unique identifier for each user.
- `movieId`: Unique identifier for each movie.
- `rating`: User’s rating (on a scale of 0.5 to 5).

##### movies.csv:

Movie metadata with:

- `movieId`: Movie identifier.
- `title`: Movie title.
- `genres`: Genres associated with the movie.

### **2.2 Data Storage & Format**

-   The dataset is stored as **CSV files**.

-   The complete dataset contains **32 million of records**, but for testing, we use a **sample of 10,000 entries**.

-   Data is loaded using `pandas` and processed into a user-item rating matrix, where:

    -   Rows represent **users**.
    -   Columns represent **movies**.
    -   Missing values (unrated movies) are replaced with **0**.

------

## **3. Methodology**

### **3.1 Recommendation Algorithm**

We use **Singular Value Decomposition (SVD)** for recommendation:

1.  Convert the ratings data into a **user-item rating matrix**.

2.  Apply 

    Truncated SVD

     from `scikit-learn`  to reduce dimensionality:

$$
R\approx U \times \Sigma \times V^T
$$


- `U`: User feature matrix.
- `Σ`: Singular values.
- `V^T`: Movie feature matrix.


3.  Predict missing ratings by computing: 

$$
\text{Predicted Ratings} = U \times V^T
$$

​    

4.  Identify **unwatched movies** and recommend the top `N=3` movies with the highest predicted ratings.

### **3.2 Implementation Details**

-   The **`model.py`** script defines the `train_svd()` function that trains the SVD model.
-   The **`recommend.py`** script uses SVD results to generate recommendations.
-   The **`main.py`** script takes a user ID as input and prints recommended movies.

------

## **4. Experimental Results**

### **4.1 Findings**

-   The system successfully predicts movie preferences for users based on historical ratings.
-   Recommendations improve as more data is available.
-   The system can efficiently handle **large datasets** but requires optimization for scalability.

### **4.2 Challenges**

-   **Cold Start Problem**: New users and movies with no prior data make predictions difficult.
-   **Computational Complexity**: SVD can become expensive with very large datasets.
-   **Limited Feature Representation**: Using only `2` latent factors (`n_components=2`) might not capture complex patterns.
-   **Group work is hard:** We met a lot of communicating issues during developing the project

### **4.3 Future Improvements**

-   **Implement IMDb API(`OMDb`)** to show more information of the movies
-   **Refactor** the current project with a better readability
    -   Allow the user to change dataset with arguments/config file

-   **Fix cold start problem**: create a recommendation system for new users:
    -   Give 5 - 10 random movies, let the user rate them (or mark as unwatched)
    -   Give top 5 top-rated unwatched movies to the user


------

## **5. Conclusion**

This project demonstrates the power of **matrix factorization (SVD)** in building an efficient recommendation system. The approach successfully provides personalized movie recommendations based on user ratings. While effective, challenges like cold start and scalability remain. Future work includes enhancing the model's predictive power and integrating alternative machine-learning techniques.