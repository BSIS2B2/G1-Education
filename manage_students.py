import streamlit as st
import pandas as pd

@st.dialog("Delete Profile")
def confirm_delete_dialog(student_names):
    """Centered confirmation modal matching the assessment exit style"""
    names_str = ", ".join(student_names)
    st.markdown(f"""
        <div style="text-align: center; padding-bottom: 10px;">
            <p style="font-size: 1.1rem; font-weight: 500; opacity: 0.9;">
                Are you sure you want to delete <b>{names_str}'s</b> entire profile? 
                This will permanently remove all their history and scores.
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
        # Changed to uppercase to match "Go Back" style
        if st.button("CANCEL", use_container_width=True):
            st.rerun()
            
    with col2:
        # Changed to uppercase to match "Go Back" style
        if st.button("CONFIRM DELETE", use_container_width=True):
            st.session_state.quiz_history = [
                r for r in st.session_state.quiz_history 
                if r['student'] not in student_names
            ]
            st.rerun()

def student_management():
    # Header color fixed to white
    st.markdown('<h2 style="color: #FFFFFF;">Student Record Management</h2>', unsafe_allow_html=True)
    
    if not st.session_state.get('quiz_history'):
        # REPLACED st.info with Bright Red Action Required Box
        st.markdown(f"""
            <div style="
                background-color: #ff4b4b1a; 
                border: 1px solid #ff4b4b4d; 
                border-left: 5px solid #ff4b4b; 
                padding: 1rem; 
                border-radius: 8px;
                margin: 10px 0;
            ">
                <div style="font-weight: 700; color: #ff4b4b;">Action Required</div>
                <div style="opacity: 0.9; color: #ffffff;">
                    No records found. Complete an assessment to see the student list.
                </div>
            </div>
        """, unsafe_allow_html=True)
        return

    df = pd.DataFrame(st.session_state.quiz_history)
    unique_students = df['student'].unique()

    st.write("Select student profiles to manage:")

    st.markdown("---")
    h_cols = st.columns([0.4, 1.5, 2.0, 0.8, 1.5, 1.2, 0.8])
    h_cols[1].markdown("**STUDENT NAME**")
    h_cols[2].markdown("**SUBJECT**")
    h_cols[3].markdown("**LEVEL**")
    h_cols[4].markdown("**NUMBER OF QUESTIONS**")
    h_cols[5].markdown("**ATTEMPT NUMBER**")
    h_cols[6].markdown("**SCORE**")
    st.markdown("---")

    to_delete = []

    diff_colors = {
        "Easy": "#00C851",
        "Medium": "#FFBB33",
        "Hard": "#FF4444"
    }

    for student in unique_students:
        student_data = df[df['student'] == student]
        num_subjects = len(student_data)
        
        with st.container():
            base_cols = st.columns([0.4, 1.5, 7.3]) 
            
            if base_cols[0].checkbox(" ", key=f"del_profile_{student}"):
                to_delete.append(student)
            
            padding = "0px"
            if num_subjects > 1:
                padding = f"{int(num_subjects * 12)}px"
            
            base_cols[1].markdown(f'''
                <div style="
                    margin-top: {padding}; 
                    font-size: clamp(0.9rem, 2.5vw, 1.3rem); 
                    font-weight: bold; 
                    word-wrap: break-word;
                    line-height: 1.2;
                ">
                    {student}
                </div>
            ''', unsafe_allow_html=True)

            with base_cols[2]:
                for idx, row in student_data.iterrows():
                    d_cols = st.columns([2.0, 0.8, 1.5, 1.2, 0.8])
                    d_cols[0].text(row['topic'])
                    
                    diff_val = row['difficulty']
                    color = diff_colors.get(diff_val, "#ffffff")
                    d_cols[1].markdown(f'<span style="color: {color}; font-weight: 600;">{diff_val}</span>', unsafe_allow_html=True)
                    
                    q_count = row.get('total_questions', 0) 
                    raw_score = row.get('score', 0)
                    att_num = row.get('attempt', 1)
                    
                    d_cols[2].text(q_count)
                    d_cols[3].text(f"{att_num:02d}")
                    d_cols[4].text(f"{int(raw_score)}/{q_count}")

            st.markdown('<div style="border-bottom: 1px solid rgba(255,255,255,0.1); margin: 10px 0;"></div>', unsafe_allow_html=True)

    st.markdown("---")
    if st.button("Delete Selected Student Profiles", use_container_width=True):
        if not to_delete:
            st.markdown(f"""
                <div style="
                    background-color: #ff4b4b1a; 
                    border: 1px solid #ff4b4b4d; 
                    border-left: 5px solid #ff4b4b; 
                    padding: 1rem; 
                    border-radius: 8px;
                    margin-top: 10px;
                ">
                    <div style="font-weight: 700; color: #ff4b4b;">Action Required</div>
                    <div style="opacity: 0.9; color: #ffffff;">Please select at least one student profile to delete.</div>
                </div>
            """, unsafe_allow_html=True)
        else:
            confirm_delete_dialog(list(set(to_delete)))