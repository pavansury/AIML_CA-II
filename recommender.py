import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_csv("dataset/movies.csv")

# TF-IDF Vectorization
tfidf = TfidfVectorizer(stop_words='english')

tfidf_matrix = tfidf.fit_transform(movies['genre'])

# Similarity matrix
similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)

def recommend(movie_name):
    movie_name = movie_name.lower()

    matches = movies[movies['title'].str.lower() == movie_name]

    if matches.empty:
        return ["Movie not found"]

    idx = matches.index[0]

    scores = list(enumerate(similarity[idx]))

    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)

    recommended_movies = []

    for i in sorted_scores[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies
