import streamlit as st
from PIL import Image
import os

st.markdown("""
<style>
.stApp {
    background-color: #edf2fa;
    font-family: 'Poppins', sans-serif;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: #abc4ff;
}

/* HEADINGS */
h1,h2,h3 {
    color: #1f2a44 !important;
}

/* HEADER CARD */
.header-card {
    background-color: #ffffff;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 15px;
    box-shadow: 0px 3px 8px rgba(0,0,0,0.05);
    border-left: 6px solid #abc4ff;
}

/* INTRO CARD */
.intro-card {
    background-color: #d7e3fc;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 20px;
    color: #1f2a44;
}

.desc-card {
    background: #ffffff;   /* ✅ CLEAN WHITE FOR READABILITY */
    padding: 15px;
    border-radius: 12px;
    margin-top: 10px;
    border-left: 6px solid #abc4ff;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.08);
    color: #1f2a44;
}

.streamlit-expanderHeader {
    background-color: #abc4ff !important;
    color: #1f2a44 !important;
    font-weight: 700 !important;
    border-radius: 8px;
}

/* Ensure expander content text is readable */
div[data-testid="stExpander"] {
    color: #1f2a44;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header-card">
    <h2 style="margin:0;">Projects</h2>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="intro-card">
    <p style="margin:0;">
        The following projects were created together with my partner <b>Jenrich Bargo</b>
            in fullfilment of our academic requirements.
    </p>
</div>
""", unsafe_allow_html=True)

projects = {
    "Project 1": {
        "desc": "Boarding House Reservation system using Python",
        "img": "image/Project1.png"
    },
    "Project 2": {
        "desc": "Mandaon Explore Zone using HTML",
        "img": "image/project3.png"
    },
    "Project 3": {
        "desc": "Voting Management System using MS Access",
        "img": "image/Project2.png"
    }
}

for title, content in projects.items():
    with st.expander(title):

        if os.path.exists(content["img"]):
            st.image(Image.open(content["img"]), width=250)
        else:
            st.warning("Image not found")

        st.markdown(f"""
        <div class="desc-card">
            <p style="margin:0;">{content["desc"]}</p>
        </div>
        """, unsafe_allow_html=True)