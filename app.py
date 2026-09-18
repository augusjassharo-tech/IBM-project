"""
app.py
Streamlit chat interface for the AI Student Support Assistant.
Run with: streamlit run app.py
"""

import streamlit as st
from agent import answer

st.set_page_config(page_title="AI Student Support Assistant", page_icon="🎓")
st.title("🎓 AI Student Support Assistant")
st.caption("Ask about college regulations, syllabus, FAQs, or notices.")

if "history" not in st.session_state:
    st.session_state.history = []

for turn in st.session_state.history:
    with st.chat_message("user"):
        st.write(turn["question"])
    with st.chat_message("assistant"):
        st.write(turn["answer"])

question = st.chat_input("Ask a question...")

if question:
    with st.chat_message("user"):
        st.write(question)

    hist_text = "\n".join(
        f"Q: {t['question']}\nA: {t['answer']}" for t in st.session_state.history
    )

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            reply = answer(question, hist_text)
        st.write(reply)

    st.session_state.history.append({"question": question, "answer": reply})
