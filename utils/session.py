import streamlit as st

def init_session_state():
    """Initialize all required session state variables"""
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = "Dashboard"
    
    if "username" not in st.session_state:
        st.session_state["username"] = ""
    
    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = [
            {"role": "assistant", "content": "Hello! I'm your agricultural assistant. How can I help you today?"}
        ]
    
    # Add other session variables as needed

def navigate_to(page_name):
    """Helper function to navigate between pages"""
    st.session_state["current_page"] = page_name
    st.rerun()