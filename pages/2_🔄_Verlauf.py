import streamlit as st


st.set_page_config(
    page_title="advotis – Verlauf",
    page_icon="assets/advotis_small.png",
    layout="centered",
)
st.sidebar.image("assets/advotis_small.png")

st.markdown("""
    # 🔄 &nbsp; Verlauf

    Hier kannst du deine vergangenen und laufenden Berichte einsehen.
""")
st.warning(
    "Diese Funktion wird in der öffentlichen Demo-Version nicht unterstützt.",
    icon="⚠️"
)
