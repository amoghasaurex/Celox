import json
import requests 
import streamlit as st
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
from appwrite.client import Client
from appwrite.services.databases import Databases

# set_page_config
st.set_page_config(page_title="Celox 🏎️", page_icon="Celox2_bg.png", layout='wide',
                   initial_sidebar_state='collapsed')

# Setting Up page configs
st.markdown("<div style='text-align: center;'><h1>Celox F1 🏎️</h1></div>", unsafe_allow_html=True)
st.write("\n")

# Defining Functions
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#lottie files
lottie_hello = load_lottiefile("F1_home.json")
lottie_why = load_lottiefile("F1_somedude.json")
# Navbar
selected = option_menu(
    menu_title=None,
    options=['Home','Our model','About us','Contact Us'],
    icons=['house','', 'book', 'envelope'],
    default_index=0,
    orientation='horizontal',
    styles=None
)

contact_form="""
<form action="https://formsubmit.co/teamceloxforms@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your Name" required>
    <input type="email" name="email" placeholder="Your Email"required>
    <textarea name="message" placeholder="Your Message"></textarea>
    <button type="submit">Send</button>
</form>
"""
# Main Page
if selected == 'Home':
    # ---Header Section--


    with st.container():

        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader('Home')
            st.write("""
                In today's world, it's more important than ever to live sustainably. But with so many different ways to reduce our environmental impact, it can be difficult to know where to start. That's where the new app, Live Green, comes in.

            Live Green is a one-stop shop for all things sustainable. It provides users with a wealth of information on how to reduce their carbon footprint, conserve resources, and live more eco-friendly lives. The app also features a variety of tools and resources to help users make sustainable choices, such as:

            A searchable database of sustainable businesses and products
            A carbon footprint calculator
            A recycling and composting guide
            Tips on how to reduce energy consumption
            A community forum where users can connect with other sustainability-minded people
            Live Green is the perfect tool for anyone who wants to live more sustainably. It's easy to use, informative, and comprehensive. With Live Green, you can make a difference for the planet, one small step at a time.""")

        with right_column:
            st_lottie(
                lottie_why,
                speed=1,
                reverse=False,
                loop=True,
                quality="low",  # medium ; high
                height=500,
                width=None,
            )

        with left_column:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st_lottie(
                lottie_hello,
                speed=1,
                reverse=False,
                loop=True,
                height=400,
            )
        with right_column:
            st.subheader("")
            st.write("""Extensive research indicates that the level of resistance one encounters when attempting to establish a habit is inversely proportional to the habit's likelihood of becoming a permanent part of their routine.
                     
At Live Green, we understand your dedication to the environment, and our mission revolves around reducing the hurdles that individuals, like yourself, often confront. Our website is dedicated to delivering an optimal array of resources and services, designed to facilitate your journey towards sustainability.
""")
            
if selected == 'Our model':
    # ---Header Section--


    with st.container():

        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader('Our Model')
    st.components.v1.iframe("https://v.creators3d.com/index.html?load=%2Fviews%2Fproduction%2Fitem%2F20240415%2F2940333525290959%2F2940333525290959.glb&autorotate=true&json-data=1713196174252&decrypt=1&tv=163", height=600, scrolling=False)

            
# Contact Page      
elif selected == "Contact Us":
    st.title("✉️ Get In Touch With Us!")
    st.markdown(contact_form, unsafe_allow_html=True)

    local_css("style/style.css")

