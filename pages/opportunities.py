import streamlit as st
from components.header import render_header, show_extra_menu
from components.back_button import back_to_dashboard
# import opportunity service here


def opportunities_page():
    render_header()
    show_extra_menu()
    st.markdown("opportunities")
    back_to_dashboard()