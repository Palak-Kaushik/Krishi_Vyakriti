"""Configuration constants for the application"""

GEE_PROJECT_ID = "precisionagriculture-454208"

# App title and branding
APP_TITLE = "VYAKRITI AGROTECH"
APP_ICON = "🌱"
APP_COLOR = "#2e7d32"

# Feature flags
ENABLE_DISEASE_DETECTION = True
ENABLE_YIELD_ESTIMATION = True
ENABLE_RESOURCE_SHARING = True
ENABLE_CHATBOT = True

# Map defaults
DEFAULT_ZOOM = 12
DEFAULT_COORDINATES = [25.6, 75.9]  # Latitude, Longitude

# Satellite indices visualization parameters
NDVI_VIS_PARAMS = {
    'min': 0,
    'max': 1,
    'palette': ['red', 'yellow', 'green']
}

NDWI_VIS_PARAMS = {
    'min': -1,
    'max': 1,
    'palette': ['brown', 'yellow', 'blue']
}

EVI_VIS_PARAMS = {
    'min': 0,
    'max': 1,
    'palette': ['red', 'yellow', 'green']
}