import streamlit as st
import pickle as pk
import requests
import confedential as c

movies = pk.load(open('movies.pkl','rb'))
vector_dis = pk.load(open('vector_dis.pkl','rb'))

def get_poster(id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{id}?api_key={c.API_KEY}&language=en-US")
    data = response.json()
    return f"https://image.tmdb.org/t/p/w500{data['poster_path']}"

def recommend(movie):
    movie_index = int(movies[movies['title'] == movie].index[0])
    recommended_movie_index = sorted(list(enumerate(vector_dis[movie_index].tolist())),reverse=True,key=lambda x:x[1])[1:6]
    indexes = [i[0] for i in recommended_movie_index]
    movie_ids = [int(movies['id'][index]) for index in indexes]
    recommended_movie = [movies['title'][index] for index in indexes]
    return recommended_movie, movie_ids


# Title of the website
st.title("Movie Recommendation System")

# Add a select box to choose a movie
selected_movie = st.selectbox(
    "Choose a Movie:",
    movies['title'].tolist()  # Example movie names
)

# Display the selected movie
st.write(f"You selected: **{selected_movie}**")

# Placeholder for recommendations
if st.button("Get Recommendations"):
    recommended_movies, movie_ids = recommend(selected_movie)
    posters = [get_poster(movie_id) for movie_id in movie_ids]

    # Create a horizontal layout
    cols = st.columns(len(recommended_movies))  # Create as many columns as there are movies

    for i, col in enumerate(cols):
        with col:  # Place content in the respective column
            col.markdown(f"<p style='text-align: center;'>{recommended_movies[i]}</p>", unsafe_allow_html=True)
            st.image(posters[i])
