import streamlit as st
import pandas as pd 
import numpy as np
from imdb import IMDb
import pickle

page_bg_img = """
<style>
    [data-testid = stHeader]{
        z-index: 000000;
    }

    [data-testid="stToolbar"]{
        z-index: 999990;
        color:black;
    }

    [data-testid = stAppViewContainer]{
        background-image : url('https://repository-images.githubusercontent.com/275336521/20d38e00-6634-11eb-9d1f-6a5232d0f84f');
        /*background-size : cover;*/
        /*opacity : 0.5;*/
    }

    [data-testid=stVerticalBlock]{
        background-color:#000000ba;
        /*background-color:#843333a1;*/
    }
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html = True)

def recommand(movie_name):
    index = np.where(movies_df.index == movie_name)[0][0]
    similar_items = sorted(list(enumerate(similarity[index])), key = lambda x : x[1], reverse = True)[1:6]
    
    ia = IMDb()

    recommended_movies = []
    recommended_movies_posters = []
    
    for i in similar_items:
        # Similar Movie
        recommended_movies.append(movies_df.index[i[0]])
        # Similar Movie Poster
        m = ia.search_movie(movies_df.index[i[0]])
        result = m[0]
        poster = dict(result)["full-size cover url"]
        recommended_movies_posters.append(poster)


    return recommended_movies, recommended_movies_posters

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies_df = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommandation System")
selected_movie_name = st.selectbox(label='Choose a Movie : ', options=movies_df.index, index=None, placeholder="Select A Movie Name...",)




if st.button('Recommand Movie'):
    names, posters = recommand(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])