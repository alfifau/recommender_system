import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('tmdb_5000_movies.csv')
df.set_index('title', inplace=True)

indices = pd.Series(df.index)
cos_sim = np.load('cosine_similarity.npy')

list_movie = []
for i in range(len(indices)):
    list_movie.append(indices[i])

def recommendations(name, cos_sim = cos_sim, indices = indices, num = 10):
    
    recommended_movie = []
    
    idx = indices[indices == name].index[0]

    score_series = pd.Series(cos_sim[idx]).sort_values(ascending = False)

    top_movies = list(score_series[1:num+1].index)
    
    for i in top_movies:
        recommended_movie.append(list(df.index)[i])
        
    return recommended_movie

st.title('Movie Recommendations')
st.write("Basically this is a content-based recommenders. It's suggest you similar movies based on a movie you like.")

chosen_movie =  st.selectbox('Your Favorite Movie', list_movie)
num_movie = st.number_input('Number of Recomendation', min_value=1, max_value=20, value=10)

if st.button('Recommend Me!'):
    movie_recomendations = pd.DataFrame(recommendations(chosen_movie, num = num_movie), columns=['Title'])
    st.write('These movies is recommended if you like to watch ', chosen_movie)
    st.dataframe(movie_recomendations)
