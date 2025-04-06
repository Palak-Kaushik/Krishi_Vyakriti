import ee
import folium
from streamlit_folium import st_folium

def initialize_earth_engine():
    """Initialize Google Earth Engine with error handling."""
    try:
        ee.Initialize(project="precisionagriculture-454208")
        print("Google Earth Engine initialized.")
        return True
    except Exception as e:
        print(f"Error initializing Earth Engine: {e}")
        return False

def get_user_coords(username):
    """Get user's farm coordinates from the database or return mock data."""
    if username:
        return [[[75.85, 25.61], [75.85, 25.71], [75.95, 25.71], [75.95, 25.61]]]
    return None

def create_map(center=None, zoom_start=10):
    """Create a base map using Folium."""
    if center is None:
        center = [25.6, 75.9]  # Default center
    return folium.Map(location=center, zoom_start=zoom_start, tiles="OpenStreetMap")


def get_farm_indices(aoi, start_date, end_date):
    try:
        if not ee.data._initialized:
            initialize_earth_engine()

        # Fetch the latest Sentinel-2 image
        s2 = (
            ee.ImageCollection("COPERNICUS/S2_HARMONIZED")
            .filterDate(start_date, end_date)
            .filterBounds(aoi)
            .filter(ee.Filter.lt("CLOUDY_PIXEL_PERCENTAGE", 20))
            .sort("system:time_start", False)  # Sort by date (latest first)
        )

        if s2.size().getInfo() == 0:
            print("No imagery available for the selected date range.")
            return None

        latest_image = s2.first()

        # Compute indices
        ndvi = latest_image.normalizedDifference(["B8", "B4"]).rename("NDVI")
        ndwi = latest_image.normalizedDifference(["B3", "B8"]).rename("NDWI")
        evi = latest_image.expression(
            "2.5 * ((NIR - RED) / (NIR + 6 * RED - 7.5 * BLUE + 1))",
            {"NIR": latest_image.select("B8"), "RED": latest_image.select("B4"), "BLUE": latest_image.select("B2")},
        ).rename("EVI")

        # Visualization parameters
        vis_params = {
            "NDVI": {"min": 0, "max": 1, "palette": ["red", "yellow", "green"]},
            "NDWI": {"min": -1, "max": 1, "palette": ["brown", "yellow", "blue"]},
            "EVI": {"min": 0, "max": 1, "palette": ["black", "blue", "green", "yellow", "red"]}
        }

        # Generate separate maps for each index
        def create_index_map(index_image, vis_param, center):
            url = index_image.getMapId(vis_param)["tile_fetcher"].url_format
            index_map = folium.Map(location=center, zoom_start=10)
            folium.raster_layers.TileLayer(url, attr="Google Earth Engine").add_to(index_map)
            return index_map

        center = [25.6, 75.9]  # Center for the map

        return {
            "ndvi_map": create_index_map(ndvi, vis_params["NDVI"], center),
            "ndwi_map": create_index_map(ndwi, vis_params["NDWI"], center),
            "evi_map": create_index_map(evi, vis_params["EVI"], center),
        }

    except Exception as e:
        print(f"Error in get_farm_indices: {e}")
        return None
