import streamlit as st
import streamlit.components.v1 as components
from render_svg import (github_icon_link, twitter_icon_link, linkedin_icon_link, medium_icon_link)

st.set_page_config(page_title="Huda Rashid", page_icon="🗿", layout="wide")

# Header
st.subheader("Huda Rashid")
st.subheader(".... ..- -.. .- .-. .- ... .... .. -..")


icon_style = """
<style>
    p {
        margin: 0;
    }
</style>
"""

# Render the CSS style in the head section
st.markdown(icon_style, unsafe_allow_html=True)

# Profiles
col1, col2, col3, col4 = st.columns(4)

col1.markdown(linkedin_icon_link, unsafe_allow_html=True)
col2.markdown(github_icon_link, unsafe_allow_html=True)
col3.markdown(twitter_icon_link, unsafe_allow_html=True)
col4.markdown(medium_icon_link, unsafe_allow_html=True)


st.divider()