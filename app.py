import streamlit as st

from render_svg import (
    icon_style, 
    github_icon_link, 
    twitter_icon_link, 
    linkedin_icon_link, 
    medium_icon_link, 
)

st.set_page_config(page_title="Huda Rashid", page_icon="🗿", layout="wide")

# Header
st.header("Huda Rashid")
st.caption("Ex-auditor turned software develper based in Sheffield, UK. Originally from Malaysia.")
st.subheader(".... ..- -.. .- .-. .- ... .... .. -..")


# Profile
st.write(icon_style, linkedin_icon_link, github_icon_link, twitter_icon_link, medium_icon_link, unsafe_allow_html=True)

st.divider()

# Skills
st.subheader("Skills and Tools")
st.write(" 💻▪️ Python ▪️ Django ▪ HTML ▪️ CSS")
st.write(" 🛢️▪️ MySQL")
st.write(" 🔨▪️ Azure ▪️ WSL")