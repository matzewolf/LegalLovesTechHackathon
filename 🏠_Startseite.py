import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(
    page_title="advotis",
    page_icon="assets/advotis_icon.png",
    layout="centered",
)
st.sidebar.image("assets/advotis_logo.png")

st.image("assets/advotis_logo.png")
st.title("🏠 &nbsp; Startseite")
page_1 = st.button("⚖️ &nbsp;&nbsp; Strafbarkeit prüfen")
if page_1:
    switch_page("Strafbarkeit_prüfen")
page_2 = st.button("🔄 &nbsp;&nbsp; Verlauf")
if page_2:
    switch_page("Verlauf")
page_3 = st.button("👥 &nbsp;&nbsp; Ansprechpartner")
if page_3:
    switch_page("Ansprechpartner")
page_4 = st.button("📖 &nbsp;&nbsp; Gesetzestexte")
if page_4:
    switch_page("Gesetzestexte")
page_5 = st.button("💡 &nbsp;&nbsp; Feedback")
if page_5:
    switch_page("Feedback")
page_6 = st.button("❔ &nbsp;&nbsp; FAQ")
if page_6:
    switch_page("FAQ")
