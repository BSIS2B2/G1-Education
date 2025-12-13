import streamlit as st
from state import init_session_state
from take_quiz import take_quiz
from analysis import performance_analysis
from leaderboard import leaderboard

st.set_page_config(
    page_title="EduQuiz",
    layout="wide"
)

init_session_state()

tabs = st.tabs([
    "Take Quiz",
    "Performance Analysis",
    "Leaderboard"
])

with tabs[0]:
    take_quiz()

with tabs[1]:
    performance_analysis()

with tabs[2]:
    leaderboard()
