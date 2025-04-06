import streamlit as st
import matplotlib.pyplot as plt
from components.header import render_header, show_extra_menu
from components.back_button import back_to_dashboard
from services.yield_service import calculate_yield

def yield_estimation_page():
    st.title("Yield Estimation")
    show_extra_menu()
    
    st.markdown("### Estimate Your Crop Yield")
    st.markdown("coming soon")
    
    back_to_dashboard()