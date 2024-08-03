# Import the chat_session from app.py
import streamlit as st
from app import chat_session

# Define the Streamlit Interface
st.set_page_config(page_title="Muichiro AI", page_icon="🗡️", layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    })
st.title("Muichiro AI 🗡️")

with st.sidebar:
    st.markdown("[View the source code](https://github.com/tinkerness/muichiro_ai)")
    st.markdown("[More info](https://en.wikipedia.org/wiki/Demon_Slayer:_Kimetsu_no_Yaiba)")


# Text input for the user to enter a place
question = st.text_input("Please enter your question on the demon slayer series: ", placeholder="e.g., Who is Tanjiro?")

if st.button("Find Answer"):
    if question:
        response = chat_session.send_message(question)
        st.markdown("### Answer")
        st.write(response.text)
    else:
        st.error("Please enter a question.")