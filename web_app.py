import streamlit as st
import numpy as np
import pandas as pd
import pickle
from utils.model_utils import get_recomendations

st.set_page_config(layout='wide')

movies = pd.read_csv('data/movies_2428.csv')
movie_dict = dict(zip(movies['title'], movies[['movieId', 'genres']].values))

# q_table = pd.read_csv('data/newqtable4.csv')
# Q = np.array(q_table.drop(columns=['Unnamed: 0']))
Q = pickle.load(open('data/qtable_compressed.pkl', 'rb'))

st.title('Movie Recommender System')
st.text('Powered by Q-Learning, created by Jacob Gottesman')
selected_movies = st.multiselect('Select some of your favorite movies', movie_dict.keys())

if len(selected_movies) > 0:

    movie_ids = [movie_dict[movie][0] for movie in selected_movies]

    recommendations = get_recomendations(Q, movie_dict, movie_ids, 5)

    df = pd.DataFrame(recommendations, columns=['title'])
    df['genres'] = df['title'].apply(lambda x: movie_dict[x][1])

    st.subheader('Recommended Movies')
    st.dataframe(df)
