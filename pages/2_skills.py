import streamlit as st

st.markdown("""
<style>
.stApp {
    background-color: #edf2fa;
    font-family: 'Poppins', sans-serif;
}
section[data-testid="stSidebar"] {
    background-color: #abc4ff;  /* 👈 change this color */
}


.block-container {
    background-color: #ffffff;
    padding: 2rem;
    border-radius: 12px;
}

h1,h2,h3 { color:#1f2a44 !important; }
p { color:#1f2a44 !important; }

.stProgress > div > div > div > div {
    background-color: #abc4ff;
}

.header-card {
    background-color: #edf2fa;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 15px;
    box-shadow: 0px 3px 8px rgba(0,0,0,0.05);
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header-card">
    <h2 style="margin:0;">Skills</h2>
</div>
""", unsafe_allow_html=True)

st.write("Python")
st.progress(50)

st.write("C")
st.progress(30)

st.write("C++")
st.progress(25)