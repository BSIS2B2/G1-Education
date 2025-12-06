import streamlit as st
import random
from datetime import datetime
import pandas as pd  # FIXED: required for charts & leaderboard

# Initialize session state
if 'students' not in st.session_state:
    st.session_state.students = {}
if 'questions' not in st.session_state:
    st.session_state.questions = []
if 'current_quiz' not in st.session_state:
    st.session_state.current_quiz = {}
if 'quiz_history' not in st.session_state:
    st.session_state.quiz_history = {}


# ======================================
# QUIZ MANAGEMENT
# ======================================
def quiz_management():
    st.header("Quiz Management")
    
    # Initialize with sample data if empty
    if not st.session_state.questions:
        initialize_sample_data()
    
    # Add new question
    with st.expander("Add New Question"):
        st.subheader("Add Question to Database")
        
        with st.form("add_question_form"):
            topic = st.selectbox("Topic", ["Professional Issues in Information System", "Individual Sports", "Entrepreneurial Mind",
                                           "Purposive Communication", "Organizatio and Management Concepts", "IT Infrastructure & Network Technologies",
                                             "Mathematics in the Modern World", "Data Stracture and Algorithms"])
            question_text = st.text_area("Question")
            options = [st.text_input(f"Option {i+1}") for i in range(4)]
            correct_answer = st.selectbox("Correct Answer", [1, 2, 3, 4])
            difficulty = st.slider("Difficulty (1-5)", 1, 5)
            
            submitted = st.form_submit_button("Add Question")
            if submitted:
                if question_text and all(options):
                    new_question = {
                        "id": len(st.session_state.questions) + 1,
                        "topic": topic,
                        "question": question_text,
                        "options": options,
                        "correct_answer": correct_answer,
                        "difficulty": difficulty
                    }
                    st.session_state.questions.append(new_question)
                    st.success("Question added successfully!")
                    st.rerun()
                else:
                    st.error("Please fill all fields")
    
    # View and manage questions
    st.subheader("Question Database")
    
    if st.session_state.questions:
        topic_filter = st.selectbox("Filter by topic", ["All"] + list(set(q["topic"] for q in st.session_state.questions)))
        
        filtered_questions = st.session_state.questions
        if topic_filter != "All":
            filtered_questions = [q for q in st.session_state.questions if q["topic"] == topic_filter]
        
        for q in filtered_questions:
            with st.expander(f"Q{q['id']}: {q['question'][:50]}..."):
                st.write(f"**Topic:** {q['topic']}")
                st.write(f"**Difficulty:** {q['difficulty']}/5")
                st.write("**Options:**")
                for i, option in enumerate(q["options"]):
                    st.write(f"{i+1}. {option}")
                st.write(f"**Correct Answer:** {q['correct_answer']}")
                
                if st.button(f"Delete Q{q['id']}", key=f"del_{q['id']}"):
                    st.session_state.questions.remove(q)
                    st.rerun()
    else:
        st.info("No questions in database. Add some questions to get started!")


def initialize_sample_data():
    sample_questions = [
        # Professional Issues in Information System
        {"id": 1, "topic": "Professional Issues in Information System", "question": "What does GDPR stand for?",
         "options": ["General Data Protection Regulation", "Global Data Privacy Rule", "General Digital Policy Rule", "Global Database Protection Regulation"],
         "correct_answer": 1, "difficulty": 3},
        {"id": 2, "topic": "Professional Issues in Information System", "question": "Which is an ethical concern in IT?",
         "options": ["Data privacy", "Cloud storage", "Coding standards", "Software licensing"],
         "correct_answer": 1, "difficulty": 2},

        # Individual Sports
        {"id": 3, "topic": "Individual Sports", "question": "Which sport is known as the 'king of sports'?",
         "options": ["Basketball", "Football", "Tennis", "Cricket"],
         "correct_answer": 2, "difficulty": 2},
        {"id": 4, "topic": "Individual Sports", "question": "The marathon distance is?",
         "options": ["42.195 km", "21 km", "50 km", "40 km"],
         "correct_answer": 1, "difficulty": 2},

        # Entrepreneurial Mind
        {"id": 5, "topic": "Entrepreneurial Mind", "question": "What is a startup?",
         "options": ["A small new business", "A multinational company", "A government project", "A charity organization"],
         "correct_answer": 1, "difficulty": 2},
        {"id": 6, "topic": "Entrepreneurial Mind", "question": "Pivoting in business means?",
         "options": ["Changing strategy", "Hiring staff", "Closing business", "Funding startup"],
         "correct_answer": 1, "difficulty": 3},

        # Purposive Communication
        {"id": 7, "topic": "Purposive Communication", "question": "Which is an example of verbal communication?",
         "options": ["Speech", "Gesture", "Facial expression", "Sign language"],
         "correct_answer": 1, "difficulty": 2},
        {"id": 8, "topic": "Purposive Communication", "question": "Active listening requires?",
         "options": ["Focus and feedback", "Talking more", "Interrupting", "Ignoring non-verbal cues"],
         "correct_answer": 1, "difficulty": 3},

        # Organization and Management Concepts
        {"id": 9, "topic": "Organizatio and Management Concepts", "question": "What is SWOT analysis used for?",
         "options": ["Assess strengths and weaknesses", "Manage employees", "Track financials", "Create schedules"],
         "correct_answer": 1, "difficulty": 3},
        {"id": 10, "topic": "Organizatio and Management Concepts", "question": "A manager who focuses on people and relationships is called?",
         "options": ["Authoritative", "Democratic", "Transactional", "Transformational"],
         "correct_answer": 2, "difficulty": 2},

        # IT Infrastructure & Network Technologies
        {"id": 11, "topic": "IT Infrastructure & Network Technologies", "question": "What does LAN stand for?",
         "options": ["Local Area Network", "Large Access Network", "Long Area Network", "Limited Area Network"],
         "correct_answer": 1, "difficulty": 2},
        {"id": 12, "topic": "IT Infrastructure & Network Technologies", "question": "IP address uniquely identifies?",
         "options": ["A device on a network", "A website", "A software", "A server room"],
         "correct_answer": 1, "difficulty": 2},

        # Mathematics in the Modern World
        {"id": 13, "topic": "Mathematics in the Modern World", "question": "Derivative of x^2?",
         "options": ["2x", "x", "x^2", "1"],
         "correct_answer": 1, "difficulty": 3},
        {"id": 14, "topic": "Mathematics in the Modern World", "question": "Pi is approximately?",
         "options": ["3.14", "2.72", "1.62", "3.41"],
         "correct_answer": 1, "difficulty": 1},

        # Data Structure and Algorithms
        {"id": 15, "topic": "Data Stracture and Algorithms", "question": "What is the time complexity of binary search?",
         "options": ["O(log n)", "O(n)", "O(n^2)", "O(1)"],
         "correct_answer": 1, "difficulty": 3},
        {"id": 16, "topic": "Data Stracture and Algorithms", "question": "Stack uses which order?",
         "options": ["LIFO", "FIFO", "Random", "Sequential"],
         "correct_answer": 1, "difficulty": 2},
    ]
    st.session_state.questions = sample_questions




# ======================================
# TAKE QUIZ
# ======================================
def take_quiz():
    st.header("📝 Take Quiz")
    
    student_name = st.text_input("Enter your name")
    
    if not student_name:
        st.warning("Please enter your name to take the quiz")
        return
    
    if student_name not in st.session_state.students:
        st.session_state.students[student_name] = []
    
    st.subheader("Quiz Settings")
    col1, col2 = st.columns(2)
    
    with col1:
        topic = st.selectbox("Select Topic", ["All"] + list(set(q["topic"] for q in st.session_state.questions)))
        num_questions = st.slider("Number of Questions", 5, min(20, len(st.session_state.questions)), 10)
    
    with col2:
        difficulty = st.slider("Difficulty Level", 1, 5, 3)
    
    if st.button("Generate Quiz"):
        generate_quiz(topic, num_questions, difficulty)
    
    if st.session_state.current_quiz:
        display_quiz(student_name)
    else:
        st.info("Click 'Generate Quiz' to start")


def generate_quiz(topic, num_questions, difficulty):
    available = st.session_state.questions
    
    if topic != "All":
        available = [q for q in available if q["topic"] == topic]
    
    min_d = max(1, difficulty - 1)
    max_d = min(5, difficulty + 1)

    available = [q for q in available if min_d <= q["difficulty"] <= max_d]
    
    if len(available) < num_questions:
        num_questions = len(available)
    
    selected = random.sample(available, num_questions)
    
    st.session_state.current_quiz = {
        "questions": selected,
        "start_time": datetime.now(),
        "student_answers": {}
    }
    
    st.success(f"Quiz generated with {num_questions} questions!")


def display_quiz(student_name):
    quiz = st.session_state.current_quiz
    questions = quiz["questions"]
    
    st.subheader(f"Quiz for {student_name}")
    
    for question in questions:
        st.write(f"### {question['question']}")
        selected = st.radio(
            "Your Answer:",
            options=range(1, 5),
            key=f"q_{question['id']}",
            horizontal=True
        )
        quiz["student_answers"][question["id"]] = selected
        st.markdown("---")
    
    if st.button("Submit Quiz"):
        submit_quiz(student_name)


def submit_quiz(student_name):
    quiz = st.session_state.current_quiz
    questions = quiz["questions"]
    answers = quiz["student_answers"]
    
    correct = 0
    topic_scores = {}
    feedback = []  # Store per-question feedback
    
    for q in questions:
        student_ans = answers.get(q["id"])
        is_correct = student_ans == q["correct_answer"]
        if is_correct:
            correct += 1
            topic_scores[q["topic"]] = topic_scores.get(q["topic"], 0) + 1
        
        feedback.append({
            "question": q["question"],
            "your_answer": q["options"][student_ans-1] if student_ans else "No answer",
            "correct_answer": q["options"][q["correct_answer"]-1],
            "is_correct": is_correct
        })
    
    total = len(questions)
    score_percent = correct / total * 100
    
    topic_avg = {}
    for topic, c in topic_scores.items():
        total_topic = len([q for q in questions if q["topic"] == topic])
        topic_avg[topic] = c / total_topic * 100
    
    result = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "total_questions": total,
        "correct_answers": correct,
        "score_percentage": score_percent,
        "topic_averages": topic_avg,
        "feedback": feedback  # store feedback for later review
    }
    
    st.session_state.quiz_history.setdefault(student_name, []).append(result)
    st.session_state.students[student_name].append(score_percent)
    
    st.success("Quiz submitted!")
    st.write(f"### Score: {score_percent:.1f}%")
    
    # Display per-question feedback
    st.subheader("✅ Quiz Feedback")
    for f in feedback:
        st.write(f"**Question:** {f['question']}")
        st.write(f"- Your Answer: {f['your_answer']}")
        st.write(f"- Correct Answer: {f['correct_answer']}")
        st.write(f"- {'Correct ✅' if f['is_correct'] else 'Incorrect ❌'}")
        st.markdown("---")
    
    st.session_state.current_quiz = {}
    st.rerun()




# ======================================
# PERFORMANCE ANALYSIS
# ======================================
def performance_analysis():
    st.header("Performance Analysis")
    
    if not st.session_state.students:
        st.info("No student data available.")
        return
    
    student = st.selectbox("Select Student", list(st.session_state.students.keys()))
    
    if not student:
        return
    
    scores = st.session_state.students[student]
    history = st.session_state.quiz_history.get(student, [])
    
    st.subheader("Score Progress")
    
    df = pd.DataFrame({
        "Quiz Number": list(range(1, len(scores)+1)),
        "Score": scores
    })
    st.line_chart(df.set_index("Quiz Number"))
    
    st.subheader("Quiz History")
    
    for i, quiz in enumerate(history, 1):
        with st.expander(f"Quiz {i} - {quiz['date']}"):
            st.write(f"Score: {quiz['score_percentage']:.1f}%")
            for topic, avg in quiz["topic_averages"].items():
                st.write(f"- {topic}: {avg:.1f}%")


# ======================================
# LEADERBOARD
# ======================================
def leaderboard():
    st.header("Leaderboard")
    
    if not st.session_state.students:
        st.info("No student data yet.")
        return
    
    averages = {s: (sum(v)/len(v) if v else 0) for s, v in st.session_state.students.items()}
    sorted_students = sorted(averages.items(), key=lambda x: x[1], reverse=True)
    
    data = [{"Rank": i+1, "Student": s, "Average Score": f"{avg:.1f}%"} 
            for i, (s, avg) in enumerate(sorted_students)]
    
    df = pd.DataFrame(data)
    st.dataframe(df, hide_index=True, use_container_width=True)


# ======================================
# MAIN APP
# ======================================
def main():
    st.set_page_config(page_title="Adaptive Quiz System", layout="wide")
    st.title("Adaptive Quiz Generator & Student Performance Analyzer")
    st.markdown("---")
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "Quiz Management", "Take Quiz", "Performance Analysis", "Leaderboard"
    ])
    
    with tab1:
        quiz_management()
    with tab2:
        take_quiz()
    with tab3:
        performance_analysis()
    with tab4:
        leaderboard()


# ENTRY POINT
if __name__ == "__main__":
    main()
