import streamlit as st


st.set_page_config(
    page_title="advotis – Information",
    page_icon="assets/advotis_small.png",
    layout="centered",
)
st.sidebar.image("assets/advotis_small.png")

st.markdown("""
    # Information
""")

stgb = st.selectbox(
    "Mich interessiert im Strafgesetzbuch (StGB)...",
    ["§ 185 Beleidigung", "§ 186 Üble Nachrede", "§ 187 Verleumdung",
    "§ 192 Beleidigung trotz Wahrheitsbeweises"]
)

if stgb == "§ 185 Beleidigung":
    st.markdown("""
        Die Beleidigung wird mit Freiheitsstrafe bis zu einem Jahr oder mit Geldstrafe und,
        wenn die Beleidigung öffentlich, in einer Versammlung,
        durch Verbreiten eines Inhalts (§ 11 Absatz 3) oder mittels einer Tätlichkeit begangen wird,
        mit Freiheitsstrafe bis zu zwei Jahren oder mit Geldstrafe bestraft.
    """)
elif stgb == "§ 186 Üble Nachrede":
    st.markdown("""
        Wer in Beziehung auf einen anderen eine Tatsache behauptet oder verbreitet,
        welche denselben verächtlich zu machen oder in der öffentlichen Meinung herabzuwürdigen geeignet ist,
        wird, wenn nicht diese Tatsache erweislich wahr ist,
        mit Freiheitsstrafe bis zu einem Jahr oder mit Geldstrafe und, wenn die Tat öffentlich, 
        in einer Versammlung oder durch Verbreiten eines Inhalts (§ 11 Absatz 3) begangen ist,
        mit Freiheitsstrafe bis zu zwei Jahren oder mit Geldstrafe bestraft.
    """)
elif stgb == "§ 187 Verleumdung":
    st.markdown("""
        Wer wider besseres Wissen in Beziehung auf einen anderen eine unwahre Tatsache behauptet oder verbreitet,
        welche denselben verächtlich zu machen oder
        in der öffentlichen Meinung herabzuwürdigen oder dessen Kredit zu gefährden geeignet ist,
        wird mit Freiheitsstrafe bis zu zwei Jahren oder mit Geldstrafe und, wenn die Tat öffentlich,
        in einer Versammlung oder durch Verbreiten eines Inhalts (§ 11 Absatz 3) begangen ist,
        mit Freiheitsstrafe bis zu fünf Jahren oder mit Geldstrafe bestraft.
    """)
elif stgb == "§ 192 Beleidigung trotz Wahrheitsbeweises":
    st.markdown("""
        Der Beweis der Wahrheit der behaupteten oder verbreiteten Tatsache schließt die Bestrafung nach § 185 nicht aus,
        wenn das Vorhandensein einer Beleidigung aus der Form der Behauptung oder Verbreitung oder aus den Umständen,
        unter welchen sie geschah, hervorgeht.
    """)
