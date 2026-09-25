import streamlit as st

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css("styles.css")

# st.markdown('', unsafe_allow_html=True)

st.markdown('<h1 id="main-heading">TEST APP</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-text">Testing Application</p>', unsafe_allow_html=True)