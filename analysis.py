import streamlit as st
import pandas as pd

def performance_analysis():
    st.header("Performance Analysis")

    if not st.session_state.quiz_history:
        st.info("No quiz data available.")
        return

    df = pd.DataFrame(st.session_state.quiz_history)

    student = st.selectbox("Select Student", sorted(df["student"].unique()))
    df = df[df["student"] == student].copy()

    st.subheader("Score Over Time")
    st.line_chart(df.set_index("date")["percentage"])

    st.subheader("Topic-wise Performance")
    topic_df = df.groupby("topic").agg({
        "score": "sum",
        "total": "sum"
    })
    topic_df["percentage"] = (topic_df["score"] / topic_df["total"]) * 100
    st.bar_chart(topic_df["percentage"])

    st.subheader("Quiz History")
    st.dataframe(
        df[["date", "topic", "difficulty", "score", "total", "percentage", "time_taken"]],
        use_container_width=True
    )
