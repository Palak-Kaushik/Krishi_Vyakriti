def get_available_resources():
    """Get list of resources available in the user's area"""

    resources = [
        {"name": "Tractor", "owner": "Rajesh Kumar", "distance": "2.5 km", "rate": "₹500/hour", "availability": "Available"},
        {"name": "Harvester", "owner": "Sunil Patel", "distance": "3.8 km", "rate": "₹1200/hour", "availability": "Available from Oct 15"},
        {"name": "Water Pump", "owner": "Amit Singh", "distance": "1.2 km", "rate": "₹200/day", "availability": "Available"},
        {"name": "Organic Fertilizer", "owner": "Community Store", "distance": "5.0 km", "rate": "₹1500/ton", "availability": "Limited Stock"},
    ]
    return resources

def submit_resource_request(resource_type, specific_resource, duration, notes):
    """Submit a resource request to the system"""
    # For demo, just return success
    if resource_type and specific_resource:
        return True
    return False