import streamlit as st
from PIL import Image

st.set_page_config(page_title="Portfolio", page_icon="🏠", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

.stApp {
    background-color: #edf2fa;
    font-family: 'Poppins', sans-serif;
}

.block-container {
    background-color: #ffffff;
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
}

/* TEXT */
h1,h2,h3 {
    color: #1f2a44 !important;
}

p,label {
    color: #2f3b52 !important;
}

/* BUTTON */
.stButton>button {
    background-color: #ccdbfd;
    color: #1f2a44;
    border-radius: 8px;
    border: 1px solid #d7e3fc;
}

/* HEADER STYLE (like About page) */
.header {
    background-color: #edf2fa;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 20px;
    border: 1px solid #d7e3fc;
}

/* PROFILE CARD */
.card {
    background-color: #ccdbfd;
    padding: 18px;
    border-radius: 12px;
    box-shadow: 0px 3px 8px rgba(0,0,0,0.04);
    border: 1px solid #d7e3fc;
}

/* INPUT RESULT CARD */
.result-card {
    background-color: #ccdbfd;
    padding: 10px;
    border-radius: 10px;
    margin-top: 10px;
    border: 1px solid #d7e3fc;
    color: #1f2a44;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: #abc4ff;
}

section[data-testid="stSidebar"] * {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header">
    <h2 style="margin:0;">Home</h2>
    <p style="margin:5px 0 0 0;">
        Welcome to my portfolio!
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div class="card">
        <h3>Hi, I'm Pen </h3>
        <p>Computer Science Student | Aspiring Developer</p>
        <p>welcome to my portfolio, this platform showcasewho I am, what i can do
                and projects i have worked on my college journey. </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    img = Image.open("image/profile.jpg")
    img = img.resize((180, 180))
    st.image(img)


name = st.text_input("Enter your name")

if st.button("Submit"):
    if name:
        st.markdown(f"""
        <div class="result-card">
            Hi {name}! Enjoy Exploring my Portfolio
        </div>
        """, unsafe_allow_html=True)