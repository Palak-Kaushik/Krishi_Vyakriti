import streamlit as st
from components.header import render_header, show_extra_menu
from utils.session import navigate_to

def dashboard_page():
    render_header()
    show_extra_menu()
    
    st.markdown("<h2 style='text-align: center; margin-bottom: 30px;'>Dashboard</h2>", unsafe_allow_html=True)
    
    st.markdown("### Insights")
    if st.button("View Agricultural Insights", key="insights_main_btn"):
        navigate_to("Insights")

    st.markdown("### Information Center?")
    if st.button("Agricultural Assistant", key="chat_btn"):
        navigate_to("Chatbot Assistant")
    
    if st.button("Opportunities", key="opportunities_btn"):
        navigate_to("Opportunities")

    st.markdown("### Other Tools")
    col1, col2, col3 = st.columns(3)
    
    with col3:
        if st.button("Disease Detection", key="disease_btn"):
            navigate_to("Disease Detection")
    
    with col2:
        if st.button("Yield Estimation", key="yield_btn"):
            navigate_to("Yield Estimation")
    
    with col1:
        if st.button("Resource Sharing", key="resource_btn"):
            navigate_to("Resource Sharing")
