import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(page_title="My website", page_icon=":tada:", layout="wide")
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Projects", "Learning ML"],
    )
if selected == "Home":
    st.title(f"Machine Learning tool for biological research")
if selected == "Projects":
    st.subheader("My ibioML Project")
if selected == "Learning ML":
    st.title(f"How does Machine Learning help analze your data")
    st.write("---")
    st.subheader("Colaborative")