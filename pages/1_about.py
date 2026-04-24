import streamlit as st

st.set_page_config(page_title="Portfolio", layout="wide")

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

h1,h2,h3 {
    color: #1f2a44 !important;
}

.card {
    background-color: #ccdbfd;
    padding: 18px;
    border-radius: 12px;
    box-shadow: 0px 3px 8px rgba(0,0,0,0.04);
    border: 1px solid #d7e3fc;
    margin-bottom: 15px; /* spacing between cards */
}

section[data-testid="stSidebar"] {
    background-color:#abc4ff;
}

.header {
    background-color: #edf2fa;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 20px;
    border: 1px solid #d7e3fc;
}

/* CARD TEXT BLACK */
.card h4,
.card p,
.card li {
    color: #000000 !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header">
    <h2 style="margin:0; color:#1f2a44;">About Me</h2>
    <p style="margin:5px 0 0 0; color:#2f3b52;">
        Get to know me, my skills, and my goals
    </p>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="card">
    <h4>About Me</h4>
    <p>
    I am someone who values growth, creativity, and hard work. I am committed to giving my full effort in everything I do, always aiming for excellence.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <h4>Achievements/Awards</h4>
    <ul>
        <li>Dean’s Lister</li>
        <li>1st Runner up in Coding Competition (2023-2024)</li>
        <li>3rd Runner up during Webdev Hackathon (2025-S3)</li>
        <li>Crypto Alchemist Award</li>
        <li>Digi Detective Award</li>
        <li>Best in Frontend Development Award</li>
    </ul>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="card">
    <h4>Goals</h4>
    <ul>
        <li>To finish my studies</li>
        <li>To get a stable job</li>
        <li>To improve my programming skills</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <h4>Education</h4>
    <ul>
        <li>
            <b>Bachelor of Science in Computer Science</b><br>
            DEBESMSCAT (2023 - Present)
        </li>
        <li>
            <b>Senior High School - GAS Strand</b><br>
            Nabongsoran High School (2022 - 2023)
        </li>
        <li>
            <b>Junior High School</b><br>
            ABC School (2017 - 2022)
        </li>
        <li>
            <b>Elementary School</b><br>
            Nabongsoran Elementary School (2010 - 202017)
        </li>
    </ul>
</div>
""", unsafe_allow_html=True)