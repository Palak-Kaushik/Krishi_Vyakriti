import streamlit as st
from components.header import render_header, show_extra_menu
from components.back_button import back_to_dashboard
from services.gee_service import get_user_coords, create_map

def land_management_page():
    st.title("Land Management")
    show_extra_menu()
    
    st.subheader("Your Agricultural Land")
    st.markdown("coming soon")
    
    
    back_to_dashboard()