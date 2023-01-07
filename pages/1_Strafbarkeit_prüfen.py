import os

import streamlit as st
import requests
from dotenv import load_dotenv


st.set_page_config(
    page_title="advotis – Strafbarkeit prüfen",
    page_icon="assets/advotis_small.png",
    layout="centered",
)
st.sidebar.image("assets/advotis_small.png")


def category_to_result_text(category: str) -> str | None:
    if category == "Beleidigung":
        return "eine **Beleidigung** nach § 185 StGB"
    elif category == "Formalbeleidigung":
        return "eine **Formalbeleidigung** nach §§ 185, 192 StGB"
    elif category == "Verleumdung":
        return "**Verleumdung** nach § 187 StGB"
    elif category == "Üble Nachrede":
        return "**Üble Nachrede** nach § 186 StGB"
    elif category == "Sonstiges":
        return "**keinen Straftatsbestand**"
    return None


st.markdown("""
    # ⚖️ &nbsp; Strafbarkeit prüfen

    Hier kannst du eine Aussage, der an dich gerichtet war, melden. Das Tool findet für dich heraus,
    ob es sich um einen potenziellen Straftatbestand handelt und wenn ja, um welchen.

    Zuerst müssen wir feststellen, ob die Anwendung deutschen Strafrechts überhaupt in Frage kommt,
    da es nur unter bestimmten Bedingungen gilt.
""")
valid = False
germany = st.selectbox(
    "Befand sich der/die Täter\*in in Deutschland, als die Aussage getätigt wurde?",
    ["", "Ja", "Nein", "Weiß ich nicht"]
)
if germany == "Ja":
    valid = True
    st.markdown("In diesem Fall gilt deutsches Strafrecht.")
elif germany == "Nein" or germany == "Weiß ich nicht":
    german = st.selectbox(
        "Ist der/die Täter\*in ein:e deutsche\*r Staatsbürger\*in oder lebt der/die Täter\*in in Deutschland?",
        ["", "Ja", "Nein", "Weiß ich nicht"]
    )
    if german == "Ja":
        valid = True
        st.markdown("In diesem Fall kommt deutsches Strafrecht in Frage.")
    elif germany == "Nein" and german == "Nein":
        st.markdown("In diesem Fall gilt deutsches Strafrecht **nicht**.")
    elif germany == "Weiß ich nicht" or german == "Weiß ich nicht":
        valid = True
        st.markdown("""
            **Möglicherweise** gilt das deutsche Strafrecht nicht in diesem Fall.
            Falls es in diesem Fall doch gilt, kannst du die nächsten Fragen beantworten.
        """)

if valid:
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
                scores = result["scores"]
                max_idx = scores.index(max(scores))
                max_category = result["labels"][max_idx]
                result_text = category_to_result_text(max_category)
                st.success(f"""
                    Die künstliche Intelligenz hat analysiert, dass es sich in diesem Fall wahrscheinlich um {result_text} handelt.
                """, icon="✅")
                st.info("""
                    Dieses Ergebnis ist eine KI-basierte Einschätzung, die nicht der Wahrheit entsprechen kann.
                    Bitte beachte, dass dieses Tool keine Rechtsberatung ersetzt.
                    Die Erstberatung, die dieses Tool bietet, kann womöglich in deinem spezifischen Einzelfall nicht zutreffen.
                    Bitte konsultiere daher immer eine qualifizierte Anwältin oder einen qualifizierten Anwalt.
                    Du kannst die dazugehörigen originalen Gesetzestexte als zusätzliche Information lesen:
                    [originale Gesetzestexte](Gesetzestexte)
                """, icon="ℹ️")
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
            st.success(f"In diesem Fall handelt es sich wahrscheinlich um {result}.", icon="✅")
            st.info("""
                Dieses Ergebnis ist nur eine vorläufige Einschätzung basierend auf deinen Eingaben.
                Bitte beachte, dass dieses Tool keine Rechtsberatung ersetzt.
                Die Erstberatung, die dieses Tool bietet, kann womöglich in deinem spezifischen Einzelfall nicht zutreffen.
                Bitte konsultiere daher immer eine qualifizierte Anwältin oder einen qualifizierten Anwalt.
                Du kannst auch die dazugehörigen originalen Gesetzestexte als zusätzliche Information lesen:
                [originale Gesetzestexte](Gesetzestexte)
            """, icon="ℹ️")
