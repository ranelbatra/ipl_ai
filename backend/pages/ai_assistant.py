import streamlit as st

from ai_assistant.loader import IPLDataLoader
from ai_assistant.analytics import CricketAnalytics
from ai_assistant.router import process_question
from ai_assistant.assistant_ai import generate_answer
from pathlib import Path


@st.cache_resource
def load_analytics():

    BASE_DIR = Path(__file__).resolve().parent.parent

    loader = IPLDataLoader(
        csv_path=BASE_DIR / "IPL_matches.csv",
        excel_path=BASE_DIR / "IPL_Data.xlsx"
    )

    return CricketAnalytics(loader)


def ai_assistant():

    st.title("🏏 AI Cricket Assistant")

    st.caption(
        "Ask questions about IPL teams, players, matches and statistics."
    )

    analytics = load_analytics()

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input
    question = st.chat_input("Ask me anything about IPL...")

    if question:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):
            st.markdown(question)

        # Get structured data
        result = process_question(
            question,
            analytics
        )

        # Generate AI explanation
        answer = generate_answer(
            question,
            result
        )

        with st.chat_message("assistant"):
            st.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )