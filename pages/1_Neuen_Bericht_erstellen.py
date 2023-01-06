import os

import streamlit as st
import requests
from dotenv import load_dotenv


st.markdown("""
    # Neuen Bericht erstellen

    Hier kannst du eine Aussage, der an dich gerichtet war, melden. Das Tool findet für dich heraus,
    ob es sich um einen potenziellen Straftatbestand handelt und wenn ja, um welchen.
""")

st.info(
    """
    Bitte beachte, dass dieses Tool keine Rechtsberatung ersetzt.
    Bitte konsultiere immer eine qualifizierte Anwältin oder einen qualifizierten Anwalt.
    Wir helfen dir dabei am Ende dieses Fragebogens.
    """,
    icon="ℹ️"
)

text = st.text_area("Gib hier die Aussage ein, die an dich gerichtet war.")
method = st.radio(
    "Welche Auswertungsmethode möchtest du verwenden?",
    ["Automatisch durch künstliche Intelligenz", "Manuell durch Fragebogen"])

if method == "Automatisch durch künstliche Intelligenz":
    start = st.button("Weiter")
    url = "https://api.firstlanguage.in/api/classify"
    load_dotenv()
    headers = {
        "Content-Type": "application/json",
        "apikey": os.getenv("FIRST_LANGUAGE_KEY")
    }
    payload = {
        "input": {
            "text": text,
            "lang": "de",
            "labels": ["Beleidigung", "Formalbeleidigung", "Üble Nachrede", "Verleumdung", "Sonstiges"]
        }
    }
    if start:
        res = requests.request("POST", url, json=payload, headers=headers)
        result = res.json()
        if res.status_code == 200:
            st.vega_lite_chart(result, use_container_width=True, spec={
                'mark': {'type': 'bar', 'tooltip': True},
                'encoding': {
                    'x': {'field': 'labels', 'type': 'nominal'},
                    'y': {'field': 'scores', 'type': 'quantitative'},
                    'color': {'field': 'labels', 'type': 'nominal'}
                }
            })
        else:
            st.error(f"Error {res.status_code}:")
            st.json(result)

elif method == "Manuell durch Fragebogen":
    result = None
    provable = st.selectbox(
        "Kann man die Aussage formal beweisen oder widerlegen?",
        ["", "Ja", "Nein"]
    )
    if provable == "Ja":
        others = st.selectbox(
            "Wurde die Aussage nur vor dir oder auch vor einer oder mehrerer anderer Personen getätigt?",
            ["", "Nur vor mir", "Auch vor einer oder mehrerer anderer Personen"]
        )
        if others == "Nur vor mir":
            true_expression = st.selectbox(
                "Ist die Aussage im Prinzip wahr, aber abwertend?",
                ["", "Ja", "Nein"]
            )
            if true_expression == "Ja":
                result = "eine **Formalbeleidigung** nach §§ 185, 192 StGB"
            elif true_expression == "Nein":
                result = "eine **Beleidigung** nach § 185 StGB"
        elif others == "Auch vor einer oder mehrerer anderer Personen":
            false_expression = st.selectbox(
                "Ist die Aussage beweisbar unwahr?",
                ["", "Ja", "Nein"]
            )
            if false_expression == "Ja":
                result = "**Verleumdung** nach § 187 StGB"
            elif false_expression == "Nein":
                result = "**Üble Nachrede** nach § 186 StGB"
    elif provable == "Nein":
        judging = st.selectbox(
            "Wertet dich die Aussage als Person herab?",
            ["", "Ja", "Nein"]
        )
        if judging == "Ja":
            result = "eine **Beleidigung** nach § 185 StGB"
        elif judging == "Nein":
            reputation = st.selectbox(
                "Schadet die Aussage deiner Reputation?",
                ["", "Ja", "Nein"]
            )
            if reputation == "Ja":
                result = "**Verleumdung** nach § 187 StGB"
            elif reputation == "Nein":
                result = "**keinen Straftatsbestand**"
    if result:
        st.markdown(f"In diesem Fall handelt es sich wahrscheinlich um {result}.")
