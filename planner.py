import sys
from airports import get_airport_coordinates
from distance import haversine
from flight_time import flight_t
from planes import get_plane_info, plane_data


def ask(prompt):
    answer = input(f"{prompt} (or q to quit): ").strip().upper()
    if answer == "Q":
        print("Goodbye!")
        sys.exit(0)
    return answer

def get_valid_plane(plane_name):
    while True:
        result = get_plane_info(plane_name)
        if result is not None:
            speed, max_range = result
            break
        else:
            print(f"Plane with name {plane_name} not found.")
            plane_name = ask("Enter the name of the plane")

    return speed, max_range, plane_name

def get_valid_airport(iata_code):
    while True:
        lat, lon = get_airport_coordinates(iata_code)
        if lat is not None and lon is not None:
            break
        else:
            print(f"Airport with IATA code {iata_code} not found.")
            iata_code = ask("Enter a valid IATA code")

    return iata_code, lat, lon



def range_check(distance, speed, max_range, plane_name):
    while True:
        if distance <= max_range:
            break
        else:
            print(f"The distance of {distance:.2f} km exceeds the plane's range of {max_range:.2f} km.")
            capable = [name for name, info in plane_data.items() if info['range'] >= distance]
            if not capable:
                print("No plane in the list has enough range for this flight.")
                sys.exit(1)
            print(f"Planes that can make this flight: {', '.join(capable)}")
            plane_name = ask("Enter the name of another plane")
            speed, max_range, plane_name = get_valid_plane(plane_name)

    return speed, max_range, plane_name


def main():
    iata_code1 = ask("Enter the IATA code of the departure airport")
    iata1, lat1, lon1 = get_valid_airport(iata_code1)
    iata_code2 = ask("Enter the IATA code of the arrival airport")
    iata2, lat2, lon2 = get_valid_airport(iata_code2)
    while iata2 == iata1:
        print("The departure and arrival airports must be different.")
        iata_code2 = ask("Enter the IATA code of the arrival airport")
        iata2, lat2, lon2 = get_valid_airport(iata_code2)
    plane_name = ask("Enter the name of the plane")
    speed, max_range, plane_name = get_valid_plane(plane_name)

    distance = haversine(lat1, lon1, lat2, lon2)
    speed, max_range, plane_name = range_check(distance, speed, max_range, plane_name)
    hours, minutes = flight_t(distance, speed)
    print(f"The flight time from {iata1} to {iata2} using the {plane_name} is approximately {hours} hours and {minutes} minutes")
    print(f"The distance between {iata1} and {iata2} is approximately {distance:.2f} km.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
