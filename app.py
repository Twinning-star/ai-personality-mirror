import streamlit as st
from questions import generate_question
from personality import analyze_personality

st.set_page_config(page_title="AI Personality Mirror", page_icon="🪞")

st.title("🪞 AI Personality Mirror")
st.caption("The mirror never lies...")

if "answers" not in st.session_state:
    st.session_state.answers = []
if "question" not in st.session_state:
    st.session_state.question = generate_question([])
if "done" not in st.session_state:
    st.session_state.done = False

if not st.session_state.done:
    st.progress(len(st.session_state.answers) / 7)
    st.markdown(f"**Question {len(st.session_state.answers) + 1} of 7**")
    st.markdown(st.session_state.question)

    choice = st.radio("Your choice:", ["A", "B", "C", "D"])

    if st.button("Next →"):
        st.session_state.answers.append(
            f"Q{len(st.session_state.answers)+1}: chose {choice}"
        )
        if len(st.session_state.answers) == 7:
            st.session_state.done = True
        else:
            st.session_state.question = generate_question(
                st.session_state.answers
            )
        st.rerun()

else:
    with st.spinner("🪞 The mirror is analyzing your soul..."):
        result = analyze_personality(st.session_state.answers)

    st.markdown("## 🪞 THE MIRROR SPEAKS")
    st.markdown(result)

    if st.button("Try Again 🔄"):
        st.session_state.answers = []
        st.session_state.question = generate_question([])
        st.session_state.done = False
        st.rerun()
