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


def validate_coordinates(lat, lon):
    """Validate latitude and longitude ranges."""
    if not (-90 <= lat <= 90):
        raise ValueError(f"Invalid latitude: {lat}. Must be between -90 and 90.")
    if not (-180 <= lon <= 180):
        raise ValueError(f"Invalid longitude: {lon}. Must be between -180 and 180.")


if __name__ == "__main__":
    # Parse command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python greatcircle.py lat1,lon1 lat2,lon2")
        sys.exit(1)

    try:
        # Read and parse input coordinates
        lat1, lon1 = map(float, sys.argv[1].split(','))
        lat2, lon2 = map(float, sys.argv[2].split(','))

        # Validate the coordinates
        validate_coordinates(lat1, lon1)
        validate_coordinates(lat2, lon2)

        # Calculate the distance
        distance = great_circle_distance(lat1, lon1, lat2, lon2)

        # Output the result
        print(f"{distance:.1f} km")
    except ValueError as e:
        # Handle invalid inputs
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        # Catch-all for unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
