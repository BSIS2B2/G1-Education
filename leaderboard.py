import streamlit as st
import pandas as pd

def leaderboard():
    """Renders the global student ranking and visualization"""
    # Header locked to white for consistency
    st.markdown('<h2 style="color: #FFFFFF; font-weight: 700;">Leaderboard</h2>', unsafe_allow_html=True)

    if not st.session_state.quiz_history:
        # UPDATED: Bright Red Alert Box instead of st.info
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
                    No data available. Complete an assessment to rank on the leaderboard.
                </div>
            </div>
        """, unsafe_allow_html=True)
        return

    # Data aggregation and processing
    df = pd.DataFrame(st.session_state.quiz_history)
    leaderboard_df = (df.groupby("student")
                      .agg(Average_Percentage=("percentage","mean"), Quizzes_Taken=("student","count"))
                      .reset_index()
                      .sort_values("Average_Percentage", ascending=False))
    
    leaderboard_df["Average_Percentage"] = leaderboard_df["Average_Percentage"].round(1)
    
    # Renamed to ALL CAPS to match Student Record Management style
    leaderboard_df = leaderboard_df.rename(columns={
        "student":"STUDENT", 
        "Average_Percentage":"AVERAGE PERCENTAGE", 
        "Quizzes_Taken":"QUIZZES TAKEN"
    })

    # UI Layout: Table and Chart
    st.markdown('<div class="card">', unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    with col1:
        st.dataframe(leaderboard_df[["STUDENT","AVERAGE PERCENTAGE","QUIZZES TAKEN"]],
                     hide_index=True,
                     use_container_width=True)
    with col2:
        # Use STUDENT as index for the chart
        st.bar_chart(leaderboard_df.set_index("STUDENT")["AVERAGE PERCENTAGE"])
    st.markdown('</div>', unsafe_allow_html=True)