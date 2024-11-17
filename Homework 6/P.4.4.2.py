""""VERY IMPORTANT: RUN THIS PROGRAM FROM TERMINAL USING THE SYNTAX IN LINE 32"""

import sys
import math

def haversine(theta):
    """Calculate the haversine of an angle in radians."""
    return math.sin(theta / 2) ** 2

def great_circle_distance(lat1, lon1, lat2, lon2, radius=6378.1):
    """Calculate the great-circle distance between two points on a sphere given their latitudes and longitudes."""
    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    
    # Apply the Haversine formula
    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1
    
    a = haversine(delta_lat) + math.cos(lat1) * math.cos(lat2) * haversine(delta_lon)
    c = 2 * math.asin(math.sqrt(a))
    
    # Distance
    distance = radius * c
    return distance

if __name__ == "__main__":
    # Parse command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python greatcircle.py 48.9,2.4 41.9,12.5")
        sys.exit(1)
    
    # Read input coordinates
    lat1, lon1 = map(float, sys.argv[1].split(','))
    lat2, lon2 = map(float, sys.argv[2].split(','))

    # Calculate the distance
    distance = great_circle_distance(lat1, lon1, lat2, lon2)
    
    # Output the result
    print(f"{distance:.1f} km")
