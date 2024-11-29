import streamlit as st
import pickle as pk

movies = pk.load(open('movies.pkl','rb'))
vector_dis = pk.load(open('vector_dis.pkl','rb'))

def recommend(movie):
    movie_index = int(movies[movies['title'] == movie].index[0])
    recommended_movie_index = sorted(list(enumerate(vector_dis[movie_index].tolist())),reverse=True,key=lambda x:x[1])[1:6]
    indexes = [i[0] for i in recommended_movie_index]
    recommended_movie = [movies['title'][index] for index in indexes]
    return recommended_movie


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
    recommended_movies = recommend(selected_movie)
    for movie in recommended_movies:
        st.write(movie)

