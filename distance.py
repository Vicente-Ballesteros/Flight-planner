from math import radians, sin, cos, sqrt, asin


radius_earth = 6371

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    km = radius_earth * c
    return km

if __name__ == "__main__":
    LHR =  (51.4700, -0.4543)
    JFK = (40.6413, -73.7781)

distance = haversine(*LHR, *JFK)
print(f"Distance between LHR and JFK: {distance:.2f} km")