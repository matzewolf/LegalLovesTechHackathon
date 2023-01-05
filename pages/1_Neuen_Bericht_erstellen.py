import streamlit as st

st.markdown("""
    # Neuen Bericht erstellen

    > Bitte beachte, dass dieses Tool keine Rechtsberatung ersetzt.
    > Bitte konsultiere immer eine qualifizierte Anwältin oder einen qualifizierten Anwalt.
    > Wir helfen dir dabei am Ende dieses Fragebogens.
""")

result = None

provable = st.selectbox(
    "Kann man die Aussage beweisen oder widerlegen?",
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
            result = "eine Formalbeleidigung"
        elif true_expression == "Nein":
            result = "eine Beleidigung"
    elif others == "Auch vor einer oder mehrerer anderer Personen":
        false_expression = st.selectbox(
            "Ist die Aussage beweisbar unwahr?",
            ["", "Ja", "Nein"]
        )
        if false_expression == "Ja":
            result = "Verleumdung"
        elif false_expression == "Nein":
            result = "Üble Nachrede"
elif provable == "Nein":
    judging = st.selectbox(
        "Wertet dich die Aussage als Person herab?",
        ["", "Ja", "Nein"]
    )
    if judging == "Ja":
        result = "eine Beleidigung"
    elif judging == "Nein":
        reputation = st.selectbox(
            "Schadet die Aussage deiner Reputation?",
            ["", "Ja", "Nein"]
        )
        if reputation == "Ja":
            result = "Verleumdung"
        elif reputation == "Nein":
            result = "keinen Straftatsbestand"

if result:
    st.write(f"In diesem Fall handelt es sich wahrscheinlich um {result}.")
