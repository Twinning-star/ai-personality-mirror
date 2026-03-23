import streamlit as st
from questions import generate_question
from personality import analyze_personality

st.set_page_config(page_title="AI Personality Mirror", page_icon="🪞", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Raleway:wght@300;400&display=swap');

html, body, [class*="css"] {
    background-color: #0a0a0f;
    color: #e0d5f5;
    font-family: 'Raleway', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #0a0a0f 0%, #1a0a2e 50%, #0a0f1a 100%);
    min-height: 100vh;
}

h1 {
    font-family: 'Cinzel', serif !important;
    color: #c9a0ff !important;
    text-align: center;
    font-size: 2.5em !important;
    text-shadow: 0 0 30px #7b2fff, 0 0 60px #7b2fff;
    letter-spacing: 4px;
}

.subtitle {
    text-align: center;
    color: #7b6a9e;
    font-style: italic;
    font-size: 1.1em;
    letter-spacing: 3px;
    margin-bottom: 30px;
}

.scenario-box {
    background: linear-gradient(135deg, #1a0a2e88, #0a0f1a88);
    border: 1px solid #7b2fff44;
    border-radius: 15px;
    padding: 25px;
    margin: 20px 0;
    box-shadow: 0 0 30px #7b2fff22, inset 0 0 30px #00000044;
    font-size: 1.1em;
    line-height: 1.8;
    color: #d4c5f9;
}

.option-btn {
    display: block;
    width: 100%;
    background: linear-gradient(135deg, #1a0a2e, #0d0d1a);
    border: 1px solid #7b2fff66;
    border-radius: 10px;
    padding: 15px 20px;
    margin: 10px 0;
    color: #c9a0ff;
    font-size: 1em;
    cursor: pointer;
    transition: all 0.3s ease;
    text-align: left;
    letter-spacing: 1px;
}

.option-btn:hover {
    background: linear-gradient(135deg, #2d1060, #1a0a3e);
    border-color: #c9a0ff;
    box-shadow: 0 0 20px #7b2fff44;
    transform: translateX(5px);
}

.result-box {
    background: linear-gradient(135deg, #1a0a2e, #0a0f1a);
    border: 1px solid #c9a0ff44;
    border-radius: 15px;
    padding: 30px;
    margin: 20px 0;
    box-shadow: 0 0 40px #7b2fff33;
}

.archetype {
    font-family: 'Cinzel', serif;
    color: #ffd700;
    font-size: 1.5em;
    text-align: center;
    text-shadow: 0 0 20px #ffd70088;
    margin-bottom: 20px;
}

.savage { color: #ff6b6b; font-style: italic; margin: 15px 0; }
.deep { color: #a0d4ff; margin: 15px 0; }
.poetic { color: #c9a0ff; font-style: italic; text-align: center; font-size: 1.1em; margin: 15px 0; }

.question-counter {
    text-align: center;
    color: #7b6a9e;
    font-size: 0.9em;
    letter-spacing: 2px;
    margin-bottom: 20px;
}

div[data-testid="stProgress"] > div {
    background: linear-gradient(90deg, #7b2fff, #c9a0ff) !important;
}

.stButton > button {
    background: linear-gradient(135deg, #2d1060, #1a0a3e) !important;
    color: #c9a0ff !important;
    border: 1px solid #7b2fff !important;
    border-radius: 10px !important;
    padding: 10px 30px !important;
    font-family: 'Cinzel', serif !important;
    letter-spacing: 2px !important;
    transition: all 0.3s !important;
    box-shadow: 0 0 15px #7b2fff44 !important;
}

.stButton > button:hover {
    box-shadow: 0 0 30px #7b2fff88 !important;
    transform: scale(1.05) !important;
}

div[data-testid="stRadio"] > label {
    color: #c9a0ff !important;
    font-size: 1em !important;
}

div[data-testid="stRadio"] div[role="radio"] {
    background: linear-gradient(135deg, #1a0a2e, #0d0d1a) !important;
    border: 1px solid #7b2fff66 !important;
    border-radius: 10px !important;
    padding: 12px 20px !important;
    margin: 8px 0 !important;
    transition: all 0.3s !important;
}
</style>
""", unsafe_allow_html=True)

# Init state
if "answers" not in st.session_state:
    st.session_state.answers = []
if "question" not in st.session_state:
    st.session_state.question = generate_question([])
if "done" not in st.session_state:
    st.session_state.done = False
if "options" not in st.session_state:
    st.session_state.options = ["A", "B", "C", "D"]

st.markdown("<h1>🪞 AI PERSONALITY MIRROR</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>✦ the mirror never lies ✦</div>", unsafe_allow_html=True)

if not st.session_state.done:
    st.progress(len(st.session_state.answers) / 7)
    st.markdown(f"<div class='question-counter'>— QUESTION {len(st.session_state.answers) + 1} OF 7 —</div>", unsafe_allow_html=True)

    lines = st.session_state.question.strip().split('\n')
    scenario = ""
    options_text = []
    for line in lines:
        if line.startswith("SCENARIO:"):
            scenario = line.replace("SCENARIO:", "").strip()
        elif line.startswith(("A)", "B)", "C)", "D)")):
            options_text.append(line.strip())

    st.markdown(f"<div class='scenario-box'>🌑 {scenario}</div>", unsafe_allow_html=True)

    if options_text:
        choice = st.radio("Choose your path:", options_text, index=0)
    else:
        choice = st.radio("Your choice:", ["A", "B", "C", "D"], index=0)

    if st.button("Continue →"):
        selected = choice[0] if choice else "A"
        st.session_state.answers.append(f"Q{len(st.session_state.answers)+1}: chose {selected}")
        if len(st.session_state.answers) == 7:
            st.session_state.done = True
        else:
            st.session_state.question = generate_question(st.session_state.answers)
        st.rerun()

else:
    with st.spinner("🪞 The mirror gazes into your soul..."):
        result = analyze_personality(st.session_state.answers)

    st.markdown("<div class='result-box'>", unsafe_allow_html=True)
    st.markdown("<h1>🪞 THE MIRROR SPEAKS</h1>", unsafe_allow_html=True)

    lines = result.strip().split('\n')
    for line in lines:
        if line.startswith("ARCHETYPE:"):
            st.markdown(f"<div class='archetype'>✦ {line.replace('ARCHETYPE:', '').strip()} ✦</div>", unsafe_allow_html=True)
        elif line.startswith("SAVAGE:"):
            st.markdown(f"<div class='savage'>💀 {line.replace('SAVAGE:', '').strip()}</div>", unsafe_allow_html=True)
        elif line.startswith("DEEP:"):
            st.markdown(f"<div class='deep'>🔮 {line.replace('DEEP:', '').strip()}</div>", unsafe_allow_html=True)
        elif line.startswith("POETIC:"):
            st.markdown(f"<div class='poetic'>✨ {line.replace('POETIC:', '').strip()}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("🔄 Try Again"):
        st.session_state.answers = []
        st.session_state.question = generate_question([])
        st.session_state.done = False
        st.rerun()
