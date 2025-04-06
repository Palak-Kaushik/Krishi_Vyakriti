def get_suggested_questions():
    """Get a list of suggested questions for the chatbot"""
    return [
        "What crops are suitable for clay soil?",
        "How to identify nutrient deficiency in wheat?",
        "Best practices for drip irrigation",
        "How to interpret my NDVI results?",
        "When should I harvest my maize crop?"
    ]

def generate_response(question):
    """Generate a response to a user question"""
    # In a real app, this would use a language model or knowledge base
    # For demo, handle a few predefined questions
    question = question.lower()
    
    if "clay soil" in question:
        return """
        Crops suitable for clay soil include:
        
        1. Rice - Thrives in water-retentive clay soils
        2. Wheat - Grows well in clay with proper drainage
        3. Cabbage & Broccoli - Can tolerate heavy soils
        4. Beans - Certain varieties do well in clay
        5. Corn/Maize - Adaptable to clay soils
        
        Before planting, consider adding organic matter to improve drainage and soil structure.
        """
    elif "nutrient deficiency" in question:
        return """
        Common nutrient deficiencies in wheat and how to identify them:
        
        1. Nitrogen: Pale yellow-green leaves, starting with older leaves. Stunted growth.
        2. Phosphorus: Dark green leaves with purple/reddish tints, especially on leaf edges.
        3. Potassium: Yellow/brown scorching along leaf edges, weak stems.
        4. Sulfur: Yellowing of younger leaves, spindly plants.
        5. Zinc: White/yellowish bands between leaf veins.
        
        Soil testing is recommended for accurate diagnosis before applying amendments.
        """
    elif "drip irrigation" in question:
        return """
        Best practices for drip irrigation:
        
        1. Install filters to prevent clogging
        2. Place emitters near the root zone (not directly on stems)
        3. Maintain consistent water pressure (10-30 PSI typically)
        4. Schedule frequent but shorter irrigation cycles
        5. Consider using pressure-compensating emitters on uneven terrain
        6. Perform regular system inspections for leaks or clogs
        7. Add a fertigation system for efficient nutrient delivery
        
        Drip irrigation can reduce water usage by 30-50% compared to flood irrigation.
        """
    elif "ndvi" in question:
        return """
        Interpreting NDVI (Normalized Difference Vegetation Index) results:
        
        - NDVI ranges from -1 to +1
        - Higher values (0.6-0.9): Dense, healthy vegetation
        - Medium values (0.2-0.5): Sparse vegetation or early growth stage
        - Low values (-0.1-0.1): Bare soil, rock, or water
        - Negative values: Water bodies, clouds, snow
        
        Compare your NDVI values to historical data for your field to identify anomalies. Sudden drops in NDVI may indicate stress, disease, or pest issues. Gradual increases typically show healthy crop development.
        """
    elif "harvest" in question:
        return """
        Determining when to harvest maize/corn:
        
        1. Dry kernel method: The corn is ready when kernels are firm and the "milk line" has disappeared. The husks should be dry and brown.
        
        2. Black layer formation: Check for the formation of a black layer at the tip of kernels (where they attach to the cob).
        
        3. Moisture content: Ideal moisture for harvesting is:
           - Grain corn: 23-25% moisture for mechanical harvesting
           - Sweet corn: Harvest when kernels are plump and produce milky juice when punctured
           
        4. Days after silking: Typically 55-65 days after silking for sweet corn, and 120-150 days after planting for grain corn.
        
        Weather conditions and variety will affect these timelines.
        """
    else:
        return "I understand you're asking about '" + question + "'. In the full application, I'd connect to an agricultural knowledge base to answer your question accurately."
