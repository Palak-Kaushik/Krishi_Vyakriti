import streamlit as st
from components.header import render_header, show_extra_menu
from components.back_button import back_to_dashboard
from services.gee_service import get_user_coords, create_map

def land_management_page():
    st.title("Land Management")
    show_extra_menu()
    
    st.subheader("Your Agricultural Land")
    st.markdown("coming soon")
    
    # user_coords = get_user_coords(st.session_state.get("username", ""))
    # m = create_map(zoom_start=12)
    
    # # Add user's land areas to the map if available
    # if user_coords:
    #     st.success(f"Showing {len(user_coords)} registered land area(s)")
    
    # st_folium(m, width="100%", height=500)
    
    back_to_dashboard()