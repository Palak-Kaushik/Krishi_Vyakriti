import streamlit as st
from PIL import Image
import time
from components.header import render_header, show_extra_menu
from components.back_button import back_to_dashboard
from services.disease_service import detect_disease

def disease_detection_page():
    """Disease detection page with image upload and analysis"""
    st.title("Crop Disease Detection")
    show_extra_menu()
    
    st.info("Upload an image of your crop leaves to detect diseases.")
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        st.write("Feature coming soon...")

    
    back_to_dashboard()