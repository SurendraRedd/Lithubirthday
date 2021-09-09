# Streamlit Timeline Component Example

import streamlit as st
from streamlit_timeline import timeline


# use full page width
st.set_page_config(page_title="BirthDay Wishes", layout="wide")

# Test/Title
st.image('https://github.com/SurendraRedd/Lithubirthday/blob/main/IMG-20210408-WA0006.jpg?raw=true',width=250)
st.markdown('# 🎂🎂🎂🎂🎂 Happy 4th Birthday Lithu')


# load data
with open('example.json', "r") as f:
    data = f.read()

# render timeline
timeline(data, height=800)
