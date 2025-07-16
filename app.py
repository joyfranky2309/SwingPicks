import streamlit as st, agent
st.set_page_config(page_title="Morning Swing Picks")
st.title("📈 Daily Momentum Scanner")
if st.button("Generate Picks"):
    with st.spinner("Analyzing..."):
        st.text(agent.get_picks())