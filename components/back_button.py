import streamlit as st
from utils.session import navigate_to

def back_to_dashboard():
    """button for back to dashboard"""
    if st.button("Back to Dashboard"):
        navigate_to("Dashboard")