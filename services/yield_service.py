def calculate_yield(crop_type, area, soil_type, irrigation, fertilizer):
    """Calculate estimated crop yield based on input parameters"""
    # Base yield ranges by crop type (tons per hectare)
    base_yields = {
        "Rice": (3.5, 6.0),
        "Wheat": (2.5, 5.0),
        "Maize": (4.0, 8.0),
        "Cotton": (1.5, 3.0),
        "Sugarcane": (60.0, 100.0),
        "Soybean": (2.0, 4.0)
    }
    
    # Simple multipliers for other factors
    soil_factors = {"Loamy": 1.1, "Sandy": 0.8, "Clay": 0.9, "Silt": 1.0, "Peaty": 0.95}
    irrigation_factors = {"Drip": 1.2, "Sprinkler": 1.1, "Flood": 0.9, "Rainfed": 0.7}
    fertilizer_factors = {"NPK": 1.1, "Urea": 1.0, "DAP": 1.05, "Organic": 0.9, "None": 0.7}
    
    # Calculate estimated yield
    min_yield, max_yield = base_yields[crop_type]
    avg_base_yield = (min_yield + max_yield) / 2
    
    estimated_yield = avg_base_yield * soil_factors[soil_type] * irrigation_factors[irrigation] * fertilizer_factors[fertilizer]
    total_yield = estimated_yield * area
    
    # Comparison data for visualization
    comparison_data = {
        'Your Estimate': estimated_yield,
        'Regional Average': avg_base_yield * 0.9,  # Fictional regional average
        'National Average': avg_base_yield * 0.8   # Fictional national average
    }
    
    return estimated_yield, total_yield, comparison_data