import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(
    page_title="advotis",
    page_icon="assets/advotis_small.png",
    layout="centered",
)
st.sidebar.image("assets/advotis_small.png")

st.image("assets/advotis_small.png")
st.title("Startseite")
page_1 = st.button(
    ":heavy_plus_sign: &nbsp;&nbsp; Strafbarkeit prüfen"
)
if page_1:
    switch_page("Strafbarkeit_prüfen")
page_2 = st.button(
    ":arrows_counterclockwise: &nbsp;&nbsp; Verlauf"
)
if page_2:
    switch_page("Verlauf")
page_3 = st.button(
    ":busts_in_silhouette: &nbsp;&nbsp; Ansprechpartner"
)
if page_3:
    switch_page("Ansprechpartner")
page_4 = st.button(
    ":book: &nbsp;&nbsp; Gesetzestexte"
)
if page_4:
    switch_page("Gesetzestexte")
page_5 = st.button(
    ":bulb: &nbsp;&nbsp; Feedback"
)
if page_5:
    switch_page("Feedback")
page_6 = st.button(
    ":grey_question: &nbsp;&nbsp; FAQ"
)
if page_5:
    switch_page("FAQ")
