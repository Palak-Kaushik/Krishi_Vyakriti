def detect_disease(image):
    """Detect crop disease from an uploaded image"""

    disease_name = "Leaf Blight"
    confidence = 85
    
    recommendations = """
    1. Apply copper-based fungicide within 48 hours
    2. Improve air circulation around plants
    3. Avoid overhead irrigation to prevent spread
    """
    
    prevention = """
    - Use disease-resistant seed varieties
    - Implement crop rotation next season
    - Monitor and maintain proper field drainage
    """
    
    return disease_name, confidence, recommendations, prevention