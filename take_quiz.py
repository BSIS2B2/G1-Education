import streamlit as st
import random
from datetime import datetime

@st.dialog("Exit Assessment")
def confirm_exit_dialog():
    """Centered confirmation modal for session termination"""
    accent_color = st.session_state.get('active_accent', '#4f46e5')
    
    st.markdown(f"""
        <div style="text-align: center; padding-bottom: 10px;">
            <p style="font-size: 1.1rem; font-weight: 500; opacity: 0.9;">
                Are you sure you want to quit? Your current progress and assessment data will be permanently terminated.
            </p>
        </div>
        <style>
            div[data-testid="stDialog"] button {{ 
                border-radius: 12px !important;
                border: none !important;
            }}
        </style>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("No", use_container_width=True):
            st.rerun()
            
    with col2:
        if st.button("Yes", use_container_width=True):
            del st.session_state.active_student
            st.session_state.current_quiz = None 
            st.rerun()

def take_quiz():
    """Main quiz controller: Handles Login, Setup, and Active Assessment"""
    accent_color = st.session_state.get('active_accent', '#4f46e5')

    if "active_student" not in st.session_state:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        name_input = st.text_input("Enter Student Name", placeholder="Type your name here")
        st.markdown('</div>', unsafe_allow_html=True)

        if not name_input:
            st.markdown(f"""
                <div style="background-color: {accent_color}1a; border: 1px solid {accent_color}4d; 
                     border-left: 5px solid {accent_color}; padding: 1rem; border-radius: 8px;">
                    <div style="font-weight: 600; color: {accent_color};">System Notice</div>
                    <div style="opacity: 0.9;">Please identify yourself to access the assessments.</div>
                </div>
                """, unsafe_allow_html=True)
            return
        
        st.session_state.active_student = name_input
        
        all_greetings = ["Welcome", "Great to see you", "Greetings", "Good luck today", "Ready to learn"]
        if "greeting_pool" not in st.session_state or not st.session_state.greeting_pool:
            st.session_state.greeting_pool = all_greetings.copy()
            random.shuffle(st.session_state.greeting_pool)
        st.session_state.current_greeting = st.session_state.greeting_pool.pop(0)
        
        if not any(s["name"] == name_input for s in st.session_state.students):
            st.session_state.students.append({"id": len(st.session_state.students)+1, "name": name_input})
        st.rerun()

    name = st.session_state.active_student.title()
    greeting = st.session_state.current_greeting
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    c1, c2 = st.columns([4, 1.2])
    with c1:
        st.markdown(f"### {greeting}, **{name}**!")
    with c2:
        if st.button("Go Back", use_container_width=True):
            confirm_exit_dialog()
    st.markdown('</div>', unsafe_allow_html=True)

    quiz = st.session_state.get("current_quiz", None)

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
                "student": name, "topic": topic, "difficulty": diff,
                "questions": selected, "answers": {}, "start_time": datetime.now(),
                "is_completed": False, "show_results": False 
            }
            for i in range(len(selected)):
                st.session_state[f"q_idx_{i}"] = None
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        return

    if not quiz["is_completed"]:
        st.markdown(f"### {quiz['topic']} Assessment")
        
        diff_map = {"Easy": "#00C851", "Medium": "#FFBB33", "Hard": "#FF4444"}
        diff_accent = diff_map.get(quiz['difficulty'], "#ffffff")
        
        total_questions = len(quiz["questions"])
        answered_count = sum(1 for i in range(total_questions) if st.session_state.get(f"q_idx_{i}") is not None)
        
        st.markdown(f'<p style="font-size: 1.4rem; font-weight: 700; margin-top: -15px;">'
                    f'<span style="color: {diff_accent};">{quiz["difficulty"]} Mode</span>, '
                    f'<span style="opacity: 0.9;">{answered_count}/{total_questions}</span></p>', 
                    unsafe_allow_html=True)
        
        st.markdown(f"<style>div[data-testid='stProgress'] > div > div > div > div {{ background-color: {diff_accent} !important; }}</style>", unsafe_allow_html=True)
        st.progress(answered_count / total_questions)
        
        for i, q in enumerate(quiz["questions"]):
            user_ans = st.session_state.get(f"q_idx_{i}")
            quiz["answers"][i] = user_ans
            
            anim_class = ""
            if quiz["show_results"]:
                correct_ans = q.get("correct_answer") or q.get("correct")
                anim_class = "correct-pulse" if user_ans == correct_ans else "wrong-shake"
            
            st.markdown(f'<div class="custom-card {anim_class}">', unsafe_allow_html=True)
            st.markdown(f"**Question {i+1}**")
            
            st.markdown(f"<style>div[role='radiogroup'] > label > div:first-child {{ border-color: {accent_color} !important; }} "
                        f"div[role='radiogroup'] > label > div:first-child > div {{ background-color: {accent_color} !important; }}</style>", 
                        unsafe_allow_html=True)

            st.radio(q["question"], q["options"], key=f"q_idx_{i}", index=None, disabled=quiz["show_results"])
            
            if quiz["show_results"]:
                correct_ans = q.get("correct_answer") or q.get("correct")
                if user_ans == correct_ans: st.success("Correct!")
                else: st.error(f"Incorrect. Answer: {correct_ans}")
            st.markdown('</div>', unsafe_allow_html=True)

        if not quiz["show_results"]:
            if st.button("Validate Answers"):
                quiz["show_results"] = True
                st.rerun()
        else:
            if st.button("Submit to Hall of Fame"):
                score = sum(1 for i, q in enumerate(quiz["questions"]) if quiz["answers"].get(i) == (q.get("correct_answer") or q.get("correct")))
                student_attempts = [r for r in st.session_state.quiz_history if r['student'] == quiz["student"] and r['topic'] == quiz["topic"]]
                attempt_num = len(student_attempts) + 1
                
                result = {
                    "student": quiz["student"], "topic": quiz["topic"], "difficulty": quiz["difficulty"],
                    "score": score, "total_questions": len(quiz["questions"]), "percentage": round((score/len(quiz["questions"]))*100),
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M"), "time_taken": (datetime.now() - quiz["start_time"]).seconds,
                    "attempt": attempt_num
                }
                st.session_state.quiz_history.append(result)
                quiz["is_completed"] = True
                st.rerun()
    
    else:
        current_student = quiz["student"]
        student_still_exists = any(r['student'] == current_student for r in st.session_state.quiz_history)

        if st.session_state.quiz_history and student_still_exists:
            student_records = [r for r in st.session_state.quiz_history if r['student'] == current_student]
            res = student_records[-1]
            st.markdown('<div class="custom-card">', unsafe_allow_html=True)
            st.markdown("### Assessment Summary")
            col1, col2, col3 = st.columns(3)
            col1.metric("Final Score", f"{res['score']} / {res['total_questions']}")
            col2.metric("Accuracy", f"{res['percentage']}%")
            col3.metric("Duration", f"{res['time_taken']}s")
            
            if res['percentage'] >= 60: st.success("Status: Passed")
            else: st.error("Status: Failed")
                
            if st.button("Start New Session"):
                for key in list(st.session_state.keys()):
                    if key.startswith("q_idx_"): del st.session_state[key]
                st.session_state.current_quiz = None
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            # UPDATED: Bright Red Action Required Box
            st.markdown(f"""
                <div style="
                    background-color: #ff4b4b1a; 
                    border: 1px solid #ff4b4b4d; 
                    border-left: 5px solid #ff4b4b; 
                    padding: 1rem; 
                    border-radius: 8px;
                    margin-bottom: 20px;
                ">
                    <div style="font-weight: 700; color: #ff4b4b;">Action Required</div>
                    <div style="opacity: 0.9; color: #ffffff;">Assessment record not found. It may have been removed from the system.</div>
                </div>
            """, unsafe_allow_html=True)
            
            if st.button("Reset Session"):
                for key in list(st.session_state.keys()):
                    if key.startswith("q_idx_"): del st.session_state[key]
                st.session_state.current_quiz = None
                st.rerun()