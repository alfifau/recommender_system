# Recommender System
Movie Recommender System is live [here](https://tmdb-movie-recommendations.herokuapp.com/)!

## Description
It's my very first project about recommender system. Basically, this is a Content-Based Recommender. It will recommends movies that are similar to a particular movie.

## Dataset
I use dataset from [Kaggle - TMDB Movie Dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata)

## Process Inside
1. Features taken from the overview column
2. Remove capitalization, punctuation, ASCII, unicode, and digit
3. Compute Term Frequency-Inverse Document Frequency (TF-IDF) vectors for each overview
4. Compute pairwise cosine similarity scores for all movies based on their overview
5. Recommend movies based on that similarity score

## Streamlit
I set it up with simple web interface using [Streamlit](https://www.streamlit.io/).
