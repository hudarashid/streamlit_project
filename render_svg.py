import streamlit as st

import base64
import textwrap

# leave as incase needed later
def render_svg(svg):
    """Renders the given svg string."""
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
    st.write(html, unsafe_allow_html=True)


# Github
github_svg_file = open("icons/github.svg","r")
g_lines = github_svg_file.readlines()
github_icon_svg =''.join(g_lines)

github_repository_url = "https://github.com/hudarashid"

github_icon_link = f'<a href="{github_repository_url}" target="_blank" rel="noopener noreferrer">{github_icon_svg}</a>'

# Twitter
twitter_svg_file = open("icons/twitter.svg","r")
t_lines = twitter_svg_file.readlines()
twitter_icon_svg=''.join(t_lines)

twitter_url = 'https://twitter.com/hudaMRashid'

twitter_icon_link = f'<a href="{twitter_url}" target="_blank" rel="noopener noreferrer">{twitter_icon_svg}</a>'

# LinkedIn
linkedin_svg_file = open("icons/linkedin.svg","r")
l_lines = linkedin_svg_file.readlines()
linkedin_icon_svg=''.join(l_lines)

linkedin_url = 'https://www.linkedin.com/in/huda-rashid-0843aa146/'

linkedin_icon_link = f'<a href="{linkedin_url}" target="_blank" rel="noopener noreferrer">{linkedin_icon_svg}</a>'

# LinkedIn
medium_svg_file = open("icons/medium.svg","r")
m_lines = medium_svg_file.readlines()
medium_icon_svg=''.join(m_lines)

medium_url = 'https://medium.com/@hudarashid'

medium_icon_link = f'<a href="{medium_url}" target="_blank" rel="noopener noreferrer">{medium_icon_svg}</a>'