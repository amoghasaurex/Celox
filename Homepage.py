import json
import requests 
import streamlit as st
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
from appwrite.client import Client
from appwrite.services.databases import Databases

# set_page_config
st.set_page_config(page_title="Team Celox 🏎️", page_icon="Celox2_bg.png", layout='wide',
                   initial_sidebar_state='collapsed')

# Setting Up page configs
st.markdown("<div style='text-align: center;'><h1>  Celox F1 🏎️</h1></div>", unsafe_allow_html=True)
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
lottiewhynot = load_lottiefile("F1-last.json")

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
    <input type="hidden" name="_next" value="https://teamcelox.streamlit.app/">
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
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.subheader('Roles and Goals')
            st.write("""
                To increase effectiveness and responsibility, we
have defined roles and duties for every team
member. The positions of Team Leader, Design
Engineer, Graphics Engineer, Production
Manager, Marketing Manager, and Sponsorship
Manager are those in our team structure. Every
team member is committed to doing their
responsibilities to the best of their ability and is
aware of what their roles are. Our main
objective is to create and produce a highperformance, innovative, and fast miniature
automobile. In order to obtain funding and
support for our project, we also want to
properly promote it to possible sponsors and
stakeholders. We hope to improve our STEM
knowledge, collaborative skills, and project
management abilities through this project.
""")

        with right_column:
            st.write("")
            st.write("")
            st_lottie(
                lottie_hello,
                speed=1,
                reverse=False,
                loop=True,
                quality="high",  # medium ; high
                height=450,
            )

        with left_column:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st_lottie(
                lottie_why,
                speed=1,
                reverse=False,
                loop=True,
                quality="high",
                height=600,
            )
            
    
        with right_column:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.subheader("Resource & Budget")
            st.write("""To guarantee optimal utilisation, we have
thoroughly evaluated our resource
requirements and distributed them
accordingly. Materials for making cars,
availability of tools and equipment, and
human resources including team members'
time and knowledge are all included in this.
A comprehensive financial plan has been
established, accounting for expenditures
related to procurement, production,
advertising, transportation, and other
incidentals. We pledge to appropriately
manage our budget so that we may
maximise the value of our expenses while
remaining within our means.
""")
        with left_column:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.subheader('Quality Control & Scope')
            st.write("""
                To increase effectiveness and responsibility, we
have defined roles and duties for every team
member. The positions of Team Leader, Design
Engineer, Graphics Engineer, Production
Manager, Marketing Manager, and Sponsorship
Manager are those in our team structure. Every
team member is committed to doing their
responsibilities to the best of their ability and is
aware of what their roles are. Our main
objective is to create and produce a highperformance, innovative, and fast miniature
automobile. In order to obtain funding and
support for our project, we also want to
properly promote it to possible sponsors and
stakeholders. We hope to improve our STEM
knowledge, collaborative skills, and project
management abilities through this project.
""")
        with right_column:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st_lottie(
                lottiewhynot,
                speed=1,
                reverse=False,
                loop=True,
                quality="high",  # medium ; high
                height=550,
                width=None,
            )
            


            
            
             
            
if selected == 'Our model':
    # ---Header Section--


    with st.container():

        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader('  ')
    st.components.v1.iframe("https://v.creators3d.com/index.html?load=%2Fviews%2Fproduction%2Fitem%2F20240417%2F2224936622320021%2F2224936622320021.glb&autorotate=true&json-data=1713340706598&decrypt=1&tv=163",height=600, scrolling=False)
    

    
if selected == 'About us':
    # ---Header Section--

    with st.container():

        left_column,centre_coulmn, right_column = st.columns(3)
        with left_column:
            st.write('')
            st.components.v1.iframe("https://gcdnb.pbrd.co/images/cvn5JJOhcuTP.png?o=1", height=500, width=1737, scrolling=False)
            st.components.v1.iframe("https://gcdnb.pbrd.co/images/9QrkmN87vjbd.png?o=1", height=850, width=1737, scrolling=False)
            
            
            
            
            
# Contact Page      
elif selected == "Contact Us":
    st.title("✉️ Get In Touch With Us!")
    st.markdown(contact_form, unsafe_allow_html=True)

    local_css("style/style.css")

