from airports import get_airport_coordinates
from distance import haversine
from flight_time import flight_t    

if __name__ == "__main__":
    iata_code1= input("Enter the IATA code of the airport: ").strip().upper()
    iata_code2= input("Enter the IATA code of the airport: ").strip().upper()
    lat, lon = get_airport_coordinates(iata_code1)
    lat2, lon2 = get_airport_coordinates(iata_code2)
    
    if lat is not None and lon is not None and lat2 is not None and lon2 is not None:
        distance = haversine(lat, lon, lat2, lon2)
        hours, minutes = flight_t(distance, 900)
        print(f"Distance between {iata_code1} and {iata_code2}: {distance:.2f} km")
        print(f"Flight time from {iata_code1} to {iata_code2}: {hours} hours and {minutes} minutes")
    else:
        print(f"Airport with IATA code {iata_code1} not found.")
        print(f"Airport with IATA code {iata_code2} not found.")