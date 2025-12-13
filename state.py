import streamlit as st

def init_session_state():
    if "questions" not in st.session_state:
        st.session_state.questions = [

            # P.I
            {
                "id": 1,
                "topic": "Professional Issues in Information System",
                "question": "What does GDPR stand for?",
                "options": ["General Data Protection Regulation", "Global Data Privacy Rule", 
                            "General Digital Policy Rule", "Global Database Protection Regulation"],
                "correct_answer": "General Data Protection Regulation",
                "difficulty": 3,
            },
            {
                "id": 2,
                "topic": "Professional Issues in Information System",
                "question": "Which is an ethical concern in IT?",
                "options": ["Data Privacy", "Cloud storage", "Coding standards", "Software licensing"],
                "correct_answer": "Data Privacy",
                "difficulty": 2,
            },
            {
                "id": 3,
                "topic": "Professional Issues in Information System",
                "question": "What is the main purpose of a code of ethics in IT professions?",
                "options": ["To guide proper professional behavior", "To increase company profit", "To limit employee creativity", "To control software updates"],
                "correct_answer": "To guide proper professional behavior",
                "difficulty": 2,
            },
            {
                "id": 4,
                "topic": "Professional Issues in Information System",
                "question": "Which principle protects users from unauthorized use of their personal data?",
                "options": ["Cloud storage", "Data Privacy", "Version Control", "Debugging"],
                "correct_answer": "Data Privacy",
                "difficulty": 3,
            },
            {
                "id": 5,
                "topic": "Professional Issues in Information System",
                "question": "When does a conflict of interest occur in the workplace?",
                "options": ["Works overtime", "Has personal gain affecting decisions", "Updates software", "Follows documentaion rules"],
                "correct_answer": "Has personal gain affecting decisions",
                "difficulty": 2,
            },

            # I.SPORTS
            {
                "id": 6,
                "topic": "Individual Sports",
                "question": "Which sport is known as the 'king of sports'",
                "options": ["Basketball", "Football", "Tennis", "Cricket"],
                "correct_answer": "Football",
                "difficulty": 2,

            },
            {
                "id": 7,
                "topic": "Individual Sports",
                "question": "The marathon distance is?",
                "options": ["42.195 km", "21 km", "50 km", "40 km"],
                "correct_answer": "42.195 km",
                "difficulty": 2,
            },
            {
                "id": 8,
                "topic": "Individual Sports",
                "question": "Which individual sport requires a racket?",
                "options": ["Swimming", "Tennis", "Running", "Taekwondo"],
                "correct_answer": "Tennis",
                "difficulty": 1,
            },
            {
                "id": 9,
                "topic": "Individual Sports",
                "question": "What is important for athletes to maintain consistency?",
                "options": ["Discipline", "Random training", "Skipping rest", "Avoiding feedback"],
                "correct_answer": "Discipline",
                "difficulty": 1,
            },
            {
                "id": 10,
                "topic": "Individual Sports",
                "question": "What does the term endurance refer to in sports?",
                "options": ["Ability to perform for long periods", "Ability to jump high", "Ability to shout loudly", "Ability to memorize"],
                "correct_answer": "Ability to perform for long periods",
                "difficulty": 2,
            },

            # ENTREP.MIND
            {
                "id": 11,
                "topic": "Entrepreneurial Mind",
                "question": "Pivoting in business means?",
                "options": ["Changing strategy", "Hiring staff", "Closing business", "Funding startup"],
                "correct_answer": "Changing strategy",
                "difficulty": 3,
            },
            {
                "id": 12,
                "topic": "Entrepreneurial Mind",
                "question": "Who is considered an entrepreneur?",
                "options": ["CAvoids risks", "Starts and manages a business", "Works as an employee", "Focuses only on theory"],
                "correct_answer": "Starts and manages a business",
                "difficulty": 2,
            },
            {
                "id": 13,
                "topic": "Entrepreneurial Mind",
                "question": "What is a startup?",
                "options": ["A small new business", "A multinational company", "A government project", "A charity organization"],
                "correct_answer": "A small new business",
                "difficulty": 2,
            },
            {
                "id": 14,
                "topic": "Entrepreneurial Mind",
                "question": "What is a innovation?",
                "options": ["Copying ideas", "Improving or creating new solutions", "Stopping development", "Removing features"],
                "correct_answer": "Improving or creating new solutions",
                "difficulty": 1,
            },
            {
                "id": 15,
                "topic": "Entrepreneurial Mind",
                "question": "What does it mean when a business changes its plan to improve?",
                "options": ["Raises product prices", "Changes its strategy", "Closes the business", "Hires new workers"],
                "correct_answer": "Changes its strategy",
                "difficulty": 1,
            },
            #PRPOSIVE COMM.
            {
                "id": 16,
                "topic": "Purposive Communication",
                "question": "Which is an example of verbal communication?",
                "options": ["Speech", "Gesture", "Facial expression", "Sign language"],
                "correct_answer": "Speech",
                "difficulty": 2,
            },
            {
                "id": 17,
                "topic": "Purposive Communication",
                "question": "What does active listening involve?",
                "options": ["Ignoring the speaker", "Giving feedback and paying attention", "Interrupting often", "Looking away"],
                "correct_answer": "Giving feedback and paying attention",
                "difficulty": 3,
            },
            {
                "id": 18,
                "topic": "Purposive Communication",
                "question": "Active listening requires?",
                "options": ["Focus and feedback", "Talking more", "Interrupting", "Ignoring non-verbal cues"],
                "correct_answer": "Focus and feedback",
                "difficulty": 3,
            },
            {
                "id": 19,
                "topic": "Purposive Communication",
                "question": "Effective communication helps reduce what?",
                "options": ["Clarity", "Coordination", "Professionalism", "Confusion"],
                "correct_answer": "Confusion",
                "difficulty": 3,
            },
            {
                "id": 20,
                "topic": "Purposive Communication",
                "question": "Which type of communication uses spoken words?",
                "options": ["Written communication", "Non-verbal", "Verbal communication", "Visual"],
                "correct_answer": "Verbal communication",
                "difficulty": 2,
            },

            # O.M
            {
                "id": 21,
                "topic": "Organization and Management Concepts",
                "question": "What does 'planning' mean in management?",
                "options": ["Acting without goals", "Ignoring changes", "Setting objectives and deciding actions", "Focusing only on problems"],
                "correct_answer": "Setting objectives and deciding actions",
                "difficulty": 2,
            },
            {
                "id": 22,
                "topic": "Organization and Management Concepts",
                "question": "Which structure groups employees by skills or function?",
                "options": ["Matrix", "Divisional", "Functional", "Horizontal"],
                "correct_answer": "Functional",
                "difficulty": 2,
            },
            {
                "id": 23,
                "topic": "Organization and Management Concepts",
                "question": "What does SWOT analysis examine?",
                "options": ["Strengths, weaknesses, opportunities, threats", "Only strengths", "Employee salaries", "Competitors only"],
                "correct_answer": "Strengths, weaknesses, opportunities, threats",
                "difficulty": 1,
            },
            {
                "id": 24,
                "topic": "Organization and Management Concepts",
                "question": "What characterizes a democratic leader?",
                "options": ["Makes decisions alone", "Encourages group participation", "Rejects feedback", "Focuses only on tasks"],
                "correct_answer": "Encourages group participation",
                "difficulty": 1,
            },
            {
                "id": 25,
                "topic": "Organization and Management Concepts",
                "question": "What does organizational culture refer to?",
                "options": ["Physical building structure", "Employee uniforms", "Shared values and beliefs", "Office layout"],
                "correct_answer": "Shared values and beliefs",
                "difficulty": 3,
            },

            #IT INFRASTRUCTURES
            {
                "id": 26,
                "topic": "IT Infrastructure & Network Technologies",
                "question": "What is the function of a router?",
                "options": ["Turns off the internet", "Runs applications", "Stores files", "Directs data between networks"],
                "correct_answer": "Directs data between networks",
                "difficulty": 3,
            },
            {
                "id": 27,
                "topic": "IT Infrastructure & Network Technologies",
                "question": "Which device connects multiple computers in a LAN?",
                "options": ["Switch", "CPU", "Modem", "Printer"],
                "correct_answer": "Switch",
                "difficulty": 2,
            },
            {
                "id": 28,
                "topic": "IT Infrastructure & Network Technologies",
                "question": "What does a firewall protect a network from?",
                "options": ["Faster downloads", "File organization", "Network attacks", "Power outage"],
                "correct_answer": "Network attacks",
                "difficulty": 2,
            },
            {
                "id": 29,
                "topic": "IT Infrastructure & Network Technologies",
                "question": "What does cloud computing allow users to do?",
                "options": ["Delete all files", "Disable networks", "Block devices", "Store data online"],
                "correct_answer": "Store data online",
                "difficulty": 3,
            },
            {
                "id": 30,
                "topic": "Organization and Management Concepts",
                "question": "What does an IP address identify?",
                "options": ["A network printer only", "A device on the network", "A Wi-Fi password", "Screen resolution"],
                "correct_answer": "A device on the network",
                "difficulty": 2,
            },

            #Math in the modern world
            {
                "id": 31,
                "topic": "Mathematics in the Modern World",
                "question": "What is the purpose of statistics?",
                "options": ["Analyze and interpret data", "Guess results randomly", "Remove data", "Create passwords"],
                "correct_answer": "Analyze and interpret data",
                "difficulty": 2,
            },
            {
                "id": 32,
                "topic": "Mathematics in the Modern World",
                "question": "What do you call a pattern that regularly repeats?",
                "options": ["Random number", "Graph", "Variable", "Sequence"],
                "correct_answer": "Sequence",
                "difficulty": 3,
            },
            {
                "id": 33,
                "topic": "Mathematics in the Modern World",
                "question": "Which of the following is an example of a Fibonacci sequence?",
                "options": ["1, 2, 4, 8", "3, 6, 9, 12", "1, 1, 2, 3", "2, 4, 6, 8"],
                "correct_answer": "1, 1, 2, 3",
                "difficulty": 3,
            },
            {
                "id": 34,
                "topic": "Mathematics in the Modern World",
                "question": "Which is an example of mathematical modeling?",
                "options": ["Using TikTok", "Predicting population growth", "Listening to music", "Sleeping early"],
                "correct_answer": "Predicting population growth",
                "difficulty": 2,
            },
            {
                "id": 35,
                "topic": "Mathematics in the Modern World",
                "question": " What does a graph help represent?",
                "options": ["Text", "Passwords", "Background images", "Numerical relationships"],
                "correct_answer": "Numerical relationships",
                "difficulty": 2,
            },

            #DSA
            {
                "id": 36,
                "topic": "Data Stractures and Algorithms",
                "question": "Which data structure follows FIFO?",
                "options": ["Queue", "Stack", "Tree", "Graph"],
                "correct_answer": "Queue",
                "difficulty": 2,
            },
            {
                "id": 37,
                "topic": "Data Stractures and Algorithms",
                "question": "What does time complexity measure??",
                "options": ["Program color", "Efficiency of an algorithm", "Number of images", "Size of hardware"],
                "correct_answer": "Efficiency of an algorithm",
                "difficulty": 3,
            },
            {
                "id": 38,
                "topic": "Data Stractures and Algorithms",
                "question": "Which is a linear data structure?",
                "options": ["Array", "Tree", "Graph", "Heap"],
                "correct_answer": "Array",
                "difficulty": 3,
            },
            {
                "id": 39,
                "topic": "Data Stractures and Algorithms",
                "question": "Which type of list is required for a binary search?",
                "options": ["Unsorted list", "Random list", "Sorted list", "Invisible data"],
                "correct_answer": "Sorted list",
                "difficulty": 3,
            },
            {
                "id": 40,
                "topic": "Data Stractures and Algorithms",
                "question": "What do you call a pattern that regularly repeats?",
                "options": ["FIFO", "Alphabetical order", "Random order", "LIFO"],
                "correct_answer": "LIFO",
                "difficulty": 3,
            },
        ]

    if "students" not in st.session_state:
        st.session_state.students = []

    if "quiz_history" not in st.session_state:
        st.session_state.quiz_history = []

    if "current_quiz" not in st.session_state:
        st.session_state.current_quiz = None
