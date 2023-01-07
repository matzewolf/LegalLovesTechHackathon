import streamlit as st


st.set_page_config(
    page_title="advotis – Feedback",
    page_icon="assets/advotis_icon.png",
    layout="centered",
)
st.sidebar.image("assets/advotis_logo.png")

st.components.v1.html("""
    <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSfMPPTQSXGc3KH7hXIiK7sH5lmKFlWoI4VrPJyDTQK55ijTfw/viewform?embedded=true" width="640" height="835" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
""",
height=835)
