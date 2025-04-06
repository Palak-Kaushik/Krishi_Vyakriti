import streamlit as st
from pages.login import login_page
from pages.dashboard import dashboard_page
from pages.land_management import land_management_page
from pages.insights import insights_page
from pages.yield_estimation import yield_estimation_page
from pages.disease_detection import disease_detection_page
from pages.resource_sharing import resource_sharing_page
from pages.chatbot import chatbot_page
from pages.opportunities import opportunities_page
from utils.session import init_session_state
from styles import load_css
import ee
try:
    ee.Initialize(project="precisionagriculture-454208")
except Exception as e:
    st.error(f"Error initializing Earth Engine: {e}")
    
def main():
    # Load custom CSS
    load_css()
    
    # Initialize session state
    init_session_state()
    
    # Determine which page to show
    if not st.session_state["logged_in"]:
        login_page()
    else:
        # Route to the appropriate page based on current_page session state
        page_mapping = {
            "Dashboard": dashboard_page,
            "Land Management": land_management_page,
            "Insights": insights_page,
            "Yield Estimation": yield_estimation_page,
            "Disease Detection": disease_detection_page,
            "Resource Sharing": resource_sharing_page,
            "Chatbot Assistant": chatbot_page,
            "Opportunities": opportunities_page
        }
        
        current_page = st.session_state.get("current_page", "Dashboard")
        page_function = page_mapping.get(current_page, dashboard_page)
        page_function()

if __name__ == "__main__":
    main()