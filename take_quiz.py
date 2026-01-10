import streamlit as st
import random
from datetime import datetime

def take_quiz():
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    name = st.text_input("Enter Student Name", placeholder="Type your name here")
    st.markdown('</div>', unsafe_allow_html=True)

    if not name:
        st.info("Welcome. Please identify yourself to access the assessments.")
        return

    # Student registration logic
    if not any(s["name"] == name for s in st.session_state.students):
        st.session_state.students.append({"id": len(st.session_state.students)+1, "name": name})

    quiz = st.session_state.get("current_quiz", None)

    # Configuration Screen
    if quiz is None:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown("### Configure Session")
        c1, c2, c3 = st.columns([2, 1, 1])
        with c1:
            topic = st.selectbox("Select Subject", sorted(st.session_state.questions.keys()))
        with c2:
            diff = st.selectbox("Select Difficulty", ["Easy", "Medium", "Hard"])
        with c3:
            count = st.select_slider("Question Count", options=[1, 3, 5, 10])
            
        if st.button("Initialize Assessment"):
            pool = st.session_state.questions[topic][diff.lower()]
            selected = random.sample(pool, min(count, len(pool)))
            st.session_state.current_quiz = {
                "student": name,
                "topic": topic,
                "difficulty": diff,
                "questions": selected,
                "answers": {},
                "start_time": datetime.now(),
                "is_completed": False
            }
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        return

    # Active Quiz Mode
    if not quiz["is_completed"]:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown(f"### {quiz['topic']} Assessment")
        
        progress = len(quiz["answers"]) / len(quiz["questions"])
        st.progress(progress)
        
        for i, q in enumerate(quiz["questions"]):
            st.markdown(f"**Question {i+1}**")
            quiz["answers"][i] = st.radio(q["question"], q["options"], key=f"q_idx_{i}", index=None)
            st.divider()

        if st.button("Submit Final Answers"):
            score = sum(1 for i, q in enumerate(quiz["questions"]) if quiz["answers"].get(i) == (q.get("correct_answer") or q.get("correct")))
            total = len(quiz["questions"])
            result = {
                "student": quiz["student"],
                "topic": quiz["topic"],
                "difficulty": quiz["difficulty"],
                "score": score,
                "total": total,
                "percentage": round((score/total)*100),
                "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "time_taken": (datetime.now() - quiz["start_time"]).seconds
            }
            st.session_state.quiz_history.append(result)
            quiz["is_completed"] = True
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # Result Summary
    else:
        res = st.session_state.quiz_history[-1]
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown("### Assessment Summary")
        col1, col2, col3 = st.columns(3)
        col1.metric("Final Score", f"{res['score']} / {res['total']}")
        col2.metric("Accuracy", f"{res['percentage']}%")
        col3.metric("Duration", f"{res['time_taken']} seconds")
        
        if res['percentage'] >= 60:
            st.success("Status: Passed")
        else:
            st.error("Status: Failed")
            
        if st.button("Start New Session"):
            st.session_state.current_quiz = None
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)