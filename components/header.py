import streamlit as st

def render_header(title="VYAKRITI AGROTECH"):
    st.markdown(f"""
    <div class="header-container">
        <h1 style='color: #2e7d32;'>{title}</h1>
        <div>
            <span style="margin-right: 10px; font-weight: bold;">Welcome, {st.session_state.get("username", "User")}!</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_extra_menu():
    with st.sidebar:
        st.subheader("Navigation")
        if st.button("Dashboard", key="nav_dashboard"):
            st.session_state["current_page"] = "Dashboard"
            st.rerun()
        
        if st.button("Profile", key="nav_profile"):
            # This would be implemented in a full application
            st.info("Profile page would be shown here")
        
        if st.button("Logout", key="nav_logout"):
            st.session_state["logged_in"] = False
            st.rerun()