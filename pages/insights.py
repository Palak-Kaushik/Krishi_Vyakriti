
import streamlit as st
import datetime
import ee
from streamlit_folium import st_folium
from services.gee_service import get_user_coords, get_farm_indices

from components.header import show_extra_menu
def insights_page():

    """Display agricultural insights using satellite data visualization."""
    st.title("Agricultural Insights")
    show_extra_menu()

    user_coords = get_user_coords(st.session_state.get("username", ""))
    if not user_coords:
        st.warning("No registered farm boundaries found. Using demo data instead.")
        aoi = ee.Geometry.Polygon([[[75.85, 25.61], [75.85, 25.71], [75.95, 25.71], [75.95, 25.61]]])
    else:
        aoi = ee.Geometry.Polygon(user_coords)


    today = datetime.date.today()
    start_date = today - datetime.timedelta(days=15)
    end_date = today


    with st.spinner("Fetching latest satellite data..."):
        indices_data = get_farm_indices(aoi, start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"))
        if indices_data:
            st.session_state.indices_data = indices_data
            st.success("Latest satellite images retrieved successfully!")


    st.markdown("### Remote Sensing Indices for Your Land")
    tab1, tab2, tab3 = st.tabs(["NDVI", "NDWI", "EVI"])

    with tab1:
        _render_index_tab("NDVI", "Normalized Difference Vegetation Index",
                          "NDVI measures vegetation health.\n- **Green**: Healthy vegetation\n- **Red**: Barren soil.",
                          "NDVI")

    with tab2:
        _render_index_tab("NDWI", "Normalized Difference Water Index",
                          "NDWI detects water stress in crops.\n- **Blue**: High water content\n- **Brown**: Dry soil.",
                          "NDWI")

    with tab3:
        _render_index_tab("EVI", "Enhanced Vegetation Index",
                          "EVI is similar to NDVI but works better in dense vegetation.\n- **Green**: Healthy crops\n- **Red**: Stressed plants.",
                          "EVI")


    if "indices_data" in st.session_state and st.session_state.indices_data:
        _render_recommendations()


def _render_index_tab(index_name, full_name, description, key):
    st.subheader(full_name)
    st.write(description)

    if "indices_data" in st.session_state and st.session_state.indices_data:
        index_map = st.session_state.indices_data.get(f"{key.lower()}_map")
        if index_map:
            st_folium(index_map, width=700, height=500, key=f"map_{key}")  # Unique key
        else:
            st.warning(f"No data available for {index_name}.")
    else:
        st.warning(f"No data available for {index_name} yet. Please check back later.")


def _render_recommendations():
    """sample recommendations."""
    st.markdown("### Analysis & Recommendations")
    st.write("""
    - **Vegetation Health**: NDVI suggests moderate to healthy vegetation.
    - **Water Availability**: NDWI highlights potential dry areas in the south.
    - **Crop Monitoring**: EVI indicates a good growth cycle for most areas.
    
    **Recommendations**:
    - Increase irrigation in dry regions.
    - Monitor stress areas for pests or nutrient deficiencies.
    - Plan harvesting based on EVI trends.
    """)

