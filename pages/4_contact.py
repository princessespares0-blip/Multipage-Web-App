import streamlit as st

st.markdown("""
<style>
.stApp {
    background-color: #edf2fa;
    font-family: 'Poppins', sans-serif;
}

/* INPUT STYLE */
input, textarea {
    background-color: #ccdbfd !important;
    border-radius: 8px !important;
    border: 1px solid #d7e3fc !important;
    color: #000000 !important;
}

/* FORCE LABEL TEXT TO BLACK */
label {
    color: #000000 !important;
    font-weight: 600 !important;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: #abc4ff;
}

/* HEADER (MATCHED WITH SKILLS DESIGN) */
.header-card {
    background-color: #edf2fa;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 15px;
    box-shadow: 0px 3px 8px rgba(0,0,0,0.05);
    border: 1px solid #d7e3fc;
}

/* BUTTON */
.stButton>button {
    background-color: #ccdbfd;
    color: #1f2a44;
    border-radius: 8px;
    border: 1px solid #d7e3fc;
}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="header-card">
    <h2 style="margin:0; color:#1f2a44;">Contact</h2>
    <p style="margin:5px 0 0 0; color:#2f3b52;">
        Feel free to message me
    </p>
</div>
""", unsafe_allow_html=True)


name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Message")

if st.button("Send"):
    if name and email and message:
        st.success("Message sent!")
    else:
        st.error("Please fill all fields")