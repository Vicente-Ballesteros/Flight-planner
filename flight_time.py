from distance import haversine

def flight_time(distance, speed):
    time = distance / speed
    hours = int(time)
    minutes = int((time - hours) * 60)
    return hours, minutes

if __name__ == "__main__":
    LHR = (51.4700, -0.4543)
    JFK = (40.6413, -73.7781)

    dist = haversine(*LHR, *JFK)
    hours, minutes = flight_time(dist, 900)
    print(f"Flight time from LHR to JFK at 900 km/h: {hours} hours and {minutes} minutes")  