import streamlit as st
from streamlit_card import card


st.set_page_config(
    page_title="advotis – Ansprechpartner",
    page_icon="assets/advotis_small.png",
    layout="centered",
)
st.sidebar.image("assets/advotis_small.png")

st.markdown("""
    # 👥 &nbsp; Ansprechpartner
""")
st.components.v1.html("""
    <div data-anw-widget="217fe44880e867"></div>
    <script async type="text/javascript" src="https://widget.anwalt.de/suche/21/baseColor/000000/buttonColor/e95d0f/headerColor/b3b3b3/width/400/rounded/1/linksNewWindow/1/disableBorder/0/get.js?uid=7fe44880e867&v=2"></script>
""", height=500)
card(
    title="HateAid",
    text="Beratungsstelle für Betroffene digitaler Gewalt",
    image="https://i.ibb.co/rp4SQ45/hateaid.png",
    url="https://hateaid.org/betroffenenberatung/",
)
card(
    title="Polizei",
    text="Onlinewachen der Polizeien der Länder",
    image="https://i.ibb.co/8xL4L8b/polizei.jpg",
    url="https://www.polizei.de/Polizei/DE/Einrichtungen/Onlinewache/onlinewache_node.html",
)
card(
    title="Gerichte und Staatsanwaltschaft",
    text="Orts- und Gerichtsverzeichnis",
    image="https://i.ibb.co/LhqyYJT/justitia.jpg",
    url="https://www.justizadressen.nrw.de/de/justiz/suche",
)
