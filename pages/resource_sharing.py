import streamlit as st
from components.header import render_header, show_extra_menu
from components.back_button import back_to_dashboard
from services.resource_service import get_available_resources, submit_resource_request

def resource_sharing_page():
    st.title("Resource Sharing")
    show_extra_menu()
    
    tab1, tab2 = st.tabs(["Available Resources", "Request Resources"])
    
    with tab1:
        st.subheader("Resources Available in Your Area")
        
        resources = get_available_resources()
        
        for i, resource in enumerate(resources):
            col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
            with col1:
                st.markdown(f"**{resource['name']}** - *{resource['owner']}*")
                st.text(f"Distance: {resource['distance']}")
            with col2:
                st.text(f"Rate: {resource['rate']}")
            with col3:
                st.text(resource['availability'])
            with col4:
                st.button(f"Request", key=f"request_{i}")
            st.divider()
    
    with tab2:
        st.subheader("Request a Resource")
        with st.form("resource_request"):
            resource_type = st.selectbox("Resource Type", ["Machinery", "Tools", "Seeds", "Fertilizer", "Labor", "Other"])
            specific_resource = st.text_input("Specific Resource")
            duration = st.text_input("Duration Required")
            notes = st.text_area("Additional Notes")
            submitted = st.form_submit_button("Submit Request")
            if submitted:
                success = submit_resource_request(resource_type, specific_resource, duration, notes)
                if success:
                    st.success("Request submitted! Nearby farmers will be notified.")
    
    back_to_dashboard()