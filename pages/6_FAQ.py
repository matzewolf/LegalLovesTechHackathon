import streamlit as st


st.set_page_config(
    page_title="advotis – Feedback",
    page_icon="assets/advotis_small.png",
    layout="centered",
)
st.sidebar.image("assets/advotis_small.png")

st.markdown("# FAQ – Häufig gestellte Fragen")
with st.expander("Was sind die nächsten Features auf der Roadmap?"):
    st.markdown("""
        - Wir wollen die künstliche Intelligenz und den Fragebogen kontinuierlich verbessern,
          sodass die Ergebnisse zuverlässiger werden.
        - Die Integration mit Beratungsstellen und Anwälten soll flüssiger laufen,
          sodass man Berichte direkt an diese senden kann.
        - Die Analyse soll um andere Straftatbestände im Internet erweitert werden, zum Beispiel Drohungen.
        - Eine Browser-Erweiterung soll in der Lage sein,
          potenzielle Verstöße aus dem Internet direkt in advotis zu importieren.
    """)
with st.expander("Wie ist dieses Tool entstanden?"):
    st.markdown("""
        Dieses Tool ist im Rahmen des [LegalLovesTech Hackathons](https://legallovestech.de/)
        vom 02.01.2023 bis 08.01.2023 entstanden.
    """)
with st.expander("Wie funktioniert das Tool technisch?"):
    st.markdown("""
        Dieses Tool wurde mit [Streamlit](http://streamlit.io/) gebaut und in Python geschrieben.
        Gehostet wird die Website in der [Streamlit Cloud](https://streamlit.io/cloud).
        Die künstliche Intelligenz basiert auf einem Service von [FirstLanguage](https://www.firstlanguage.in/).
        Seh dir gerne den Code auf [GitHub](https://github.com/matzewolf/LegalLovesTechHackathon) an.
    """)
