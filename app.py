import streamlit as st
from state import init_session_state
from take_quiz import take_quiz
from analysis import performance_analysis
from leaderboard import leaderboard

st.set_page_config(page_title="QuizLearn Professional", layout="wide", initial_sidebar_state="collapsed")

# High-Fidelity UI Styling
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
        background-color: #0b0e14;
    }

    /* Gradient Title */
    .app-title {
        background: linear-gradient(90deg, #ffffff 0%, #a3c4f3 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 48px;
        font-weight: 800;
        margin-bottom: 5px;
        letter-spacing: -2px;
    }

    .subtitle {
        color: #64748b;
        margin-bottom: 30px;
        font-size: 16px;
    }

    /* Glass Card styling for all containers */
    .custom-card {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(20px);
        border-radius: 24px;
        padding: 40px;
        margin-bottom: 25px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.5);
    }

    /* Modern Buttons */
    div.stButton > button {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: white;
        border: none;
        padding: 15px 30px;
        border-radius: 14px;
        font-weight: 700;
        transition: 0.4s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
        width: 100%;
    }

    div.stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 20px rgba(99, 102, 241, 0.4);
        color: white;
    }

    /* Tab navigation styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }

    .stTabs [data-baseweb="tab"] {
        height: 50px;
        color: #808495;
        font-weight: 600;
    }

    .stTabs [aria-selected="true"] {
        color: #6366f1 !important;
        border-bottom-color: #6366f1 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="app-title">QuizLearn</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Master your craft through interactive assessment.</div>', unsafe_allow_html=True)

init_session_state()

tabs = st.tabs(["Assessment", "Analytics", "Hall of Fame"])

with tabs[0]:
    take_quiz()

with tabs[1]:
    performance_analysis()

with tabs[2]:
    leaderboard()