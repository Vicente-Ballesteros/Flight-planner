from airports import get_airport_coordinates
from distance import haversine
from flight_time import flight_t    
from planes import get_plane_info  

def get_valid_plane(plane_name):
    while True:
        result = get_plane_info(plane_name)
        if result is not None:
            speed, range = result
            break
        else:
            print(f"Plane with name {plane_name} not found.")
            plane_name = input("Enter the name of the plane: ").strip().upper()

    return speed, range, plane_name

def get_valid_airport(iata_code):
    while True:
        lat, lon = get_airport_coordinates(iata_code)
        if lat is not None and lon is not None:
            break
        else:
            print(f"Airport with IATA code {iata_code} not found.")
            iata_code = input("Enter the IATA code of the airport: ").strip().upper()

    return iata_code, lat, lon


def range_check(distance, range):
    if distance > range:
        print(f"Warning: The distance of {distance:.2f} km exceeds the plane's range of {range:.2f} km.")
    else:
        print(f"The distance of {distance:.2f} km is within the plane's range of {range:.2f} km.")

if __name__ == "__main__":
    iata_code1= input("Enter the IATA code of the airport: ").strip().upper()
    iata_code2= input("Enter the IATA code of the airport: ").strip().upper()
    iata1, lat1, lon1 = get_valid_airport(iata_code1)
    iata2, lat2, lon2 = get_valid_airport(iata_code2)
    plane_name = input("Enter the name of the plane: ").strip().upper()
    speed, range, plane_name = get_valid_plane(plane_name)

    distance = haversine(lat1, lon1, lat2, lon2)
    hours, minutes = flight_t(distance, speed)
    print(f"The flight time from {iata1} to {iata2} using the {plane_name} is approximately {hours} hours and {minutes} minutes.")
    range_check(distance, range)

