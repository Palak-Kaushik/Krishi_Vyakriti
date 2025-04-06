import streamlit as st

def login_page():
    """Login page with authentication"""
    st.title("VYAKRITI AGROTECH")
    
    st.markdown("### Login (DEMO)")
    
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")
        
        if submit:
            #   dummy login
            if username and password:  
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.rerun()
            else:
                st.error("Invalid username or password")
