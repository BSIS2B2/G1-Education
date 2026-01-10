import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def draw_gauge_chart(percentage, topic_name):
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = percentage,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': topic_name, 'font': {'size': 18, 'color': 'white'}},
        gauge = {
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "white"},
            'bar': {'color': "#6366f1"},
            'bgcolor': "rgba(0,0,0,0)",
            'borderwidth': 2,
            'bordercolor': "rgba(255,255,255,0.1)"
        }
    ))
    fig.update_layout(
        height=220, 
        margin=dict(l=20, r=20, t=50, b=20), 
        paper_bgcolor='rgba(0,0,0,0)',
        font={'color': "white", 'family': "Plus Jakarta Sans"}
    )
    return fig

def performance_analysis():
    if not st.session_state.quiz_history:
        st.info("No data available. Complete an assessment to see analytics.")
        return

    df = pd.DataFrame(st.session_state.quiz_history)
    selected_user = st.selectbox("Select Student Profile", df["student"].unique())
    user_df = df[df["student"] == selected_user]

    st.markdown(f"### Performance Metrics for {selected_user}")
    
    # Gauge Charts for Topic Mastery
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.markdown("#### Topic Mastery Level")
    topic_summary = user_df.groupby("topic")["percentage"].mean().reset_index()
    gauge_cols = st.columns(len(topic_summary))
    
    for idx, row in topic_summary.iterrows():
        with gauge_cols[idx]:
            st.plotly_chart(draw_gauge_chart(row['percentage'], row['topic']), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Historical Line Chart
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.markdown("#### Score Progression Over Time")
    line_fig = px.line(user_df, x="date", y="percentage", markers=True, template="plotly_dark")
    line_fig.update_traces(line_color='#a855f7', marker=dict(size=10))
    line_fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis_title="Date of Assessment",
        yaxis_title="Percentage Score"
    )
    st.plotly_chart(line_fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)