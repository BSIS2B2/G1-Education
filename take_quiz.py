import streamlit as st
import random
from datetime import datetime

PASSING_SCORE = 60  # %

def take_quiz():
    st.header("Take Quiz")

    name = st.text_input("Enter your name")

    if not name:
        st.info("Please enter your name to continue.")
        return

    # Register user
    if not any(s["name"] == name for s in st.session_state.students):
        st.session_state.students.append({
            "id": len(st.session_state.students) + 1,
            "name": name
        })

    quiz = st.session_state.current_quiz

    # ================= QUIZ SETUP =================
    if quiz is None:
        st.subheader("Quiz Setup")

        topics = sorted(set(q["topic"] for q in st.session_state.questions))
        topic = st.selectbox("Select Topic", topics)
        difficulty = st.slider("Difficulty", 1, 5, 1)
        num_questions = st.slider("Number of Questions", 1, 20, 10)

        if st.button("Start Quiz"):
            pool = [
                q for q in st.session_state.questions
                if q["topic"] == topic and q["difficulty"] == difficulty
            ]

            if not pool:
                st.warning("No questions available for this selection.")
                return

            questions = random.sample(pool, min(num_questions, len(pool)))

            # Shuffle options ONCE
            shuffled_options = {}
            for q in questions:
                opts = q["options"].copy()
                random.shuffle(opts)
                shuffled_options[q["id"]] = opts

            st.session_state.current_quiz = {
                "student": name,
                "topic": topic,
                "difficulty": difficulty,
                "questions": questions,
                "options": shuffled_options,
                "answers": {},
                "start_time": datetime.now(),
                "submitted": False
            }

            st.rerun()

        return  # Stop here if no quiz yet

    # ================= SIDEBAR INFO =================
    with st.sidebar:
        st.subheader("Quiz Info")
        st.write(f"Student: {quiz['student']}")
        st.write(f"Topic: {quiz['topic']}")
        st.write(f"Difficulty: {quiz['difficulty']}")
        st.write(f"Total Questions: {len(quiz['questions'])}")

    # ================= QUIZ IN PROGRESS =================
    if quiz and not quiz["submitted"]:
        st.subheader("Quiz In Progress")

        progress = len(quiz["answers"]) / len(quiz["questions"])
        st.progress(progress)

        for i, q in enumerate(quiz["questions"], start=1):
            st.markdown(f"**Question {i} of {len(quiz['questions'])}**")

            quiz["answers"][q["id"]] = st.radio(
                q["question"],
                quiz["options"][q["id"]],
                key=f"q_{q['id']}"
            )

            st.divider()

        if st.button("Submit Quiz"):
            score = sum(
                1 for q in quiz["questions"]
                if quiz["answers"].get(q["id"]) == q["correct_answer"]
            )

            time_taken = (datetime.now() - quiz["start_time"]).seconds
            percentage = (score / len(quiz["questions"])) * 100

            st.session_state.quiz_history.append({
                "student": quiz["student"],
                "topic": quiz["topic"],
                "difficulty": quiz["difficulty"],
                "score": score,
                "total": len(quiz["questions"]),
                "percentage": percentage,
                "time_taken": time_taken,
                "date": datetime.now()
            })

            quiz["submitted"] = True
            st.rerun()

    # ================= QUIZ RESULTS =================
    if quiz and quiz["submitted"]:
        last = st.session_state.quiz_history[-1]

        st.subheader("Quiz Results")

        col1, col2, col3 = st.columns(3)
        col1.metric("Score", f"{last['score']} / {last['total']}")
        col2.metric("Percentage", f"{last['percentage']:.1f}%")
        col3.metric("Time Taken", f"{last['time_taken']} sec")

        if last["percentage"] >= PASSING_SCORE:
            st.success("Status: PASSED")
        else:
            st.error("Status: FAILED")

        with st.expander("Review Answers"):
            for q in quiz["questions"]:
                user_answer = quiz["answers"].get(q["id"])

                st.markdown(f"**{q['question']}**")
                st.write(f"Your answer: {user_answer}")
                st.write(f"Correct answer: {q['correct_answer']}")

                if user_answer == q["correct_answer"]:
                    st.success("Correct")
                else:
                    st.error("Incorrect")

                st.divider()

        if st.button("Start New Quiz"):
            st.session_state.current_quiz = None
            st.rerun()
