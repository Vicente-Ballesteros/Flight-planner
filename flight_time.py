def flight_t(distance, speed):
    time = distance / speed
    hours, minutes = divmod(round(time * 60), 60)
    return hours, minutes

