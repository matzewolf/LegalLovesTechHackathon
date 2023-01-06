import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.sidebar.image("assets/advotis_small.png")

st.title("advotis Startseite")

page_1 = st.button(
    ":heavy_plus_sign: &nbsp;&nbsp; Neuen Bericht erstellen",
)
if page_1:
    switch_page("Neuen_Bericht_erstellen")

page_2 = st.button(
    ":arrows_counterclockwise: &nbsp;&nbsp; Verlauf",
)
if page_2:
    switch_page("Verlauf")

page_3 = st.button(
    ":busts_in_silhouette: &nbsp;&nbsp; Ansprechpartner",
)
if page_3:
    switch_page("Ansprechpartner")

page_4 = st.button(
    ":information_source: &nbsp;&nbsp; Information",
)
if page_4:
    switch_page("Information")
