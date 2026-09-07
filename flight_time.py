from distance import haversine

def flight_t(distance, speed):
    time = distance / speed
    hours = int(time)
    minutes = int((time - hours) * 60)
    return hours, minutes

