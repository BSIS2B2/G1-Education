import streamlit as st
import pandas as pd

def leaderboard():
    st.header("Leaderboard")

    if not st.session_state.quiz_history:
        st.info("No data available.")
        return

    df = pd.DataFrame(st.session_state.quiz_history)

    leaderboard_df = (
        df.groupby("student")
        .agg(
            avg_percentage=("percentage", "mean"),
            quizzes_taken=("student", "count")
        )
        .reset_index()
        .sort_values("avg_percentage", ascending=False)
    )

    leaderboard_df["Average Percentage"] = leaderboard_df["avg_percentage"].round(1)

    st.dataframe(leaderboard_df, use_container_width=True)
    st.bar_chart(leaderboard_df.set_index("student")["avg_percentage"])
