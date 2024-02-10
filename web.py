import streamlit as st
import functions

shows = functions.get_shows('showlist.txt')

def add_show():
    new_show = st.session_state['new_show'] + '\n'
    shows.append(new_show)
    functions.write_shows(shows)
    st.session_state['new_show'] = ''


st.title("Netflix Shows & Movies")
st.write("This app contains the list of good shows & movies to watch on Netflix")

for index, show in enumerate(shows):
    checkbox = st.checkbox(show, key=show)
    if checkbox:
        shows.pop(index)
        functions.write_shows(shows)
        del st.session_state[show]
        st.experimental_rerun()

st.text_input(label='', placeholder="Add a new show or movie to the list...",
              on_change=add_show, key='new_show')

