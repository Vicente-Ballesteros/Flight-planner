import airportsdata
from distance import haversine

def get_airport_coordinates(iata_code):
    airport_data = airportsdata.load('IATA')
    if iata_code in airport_data:
        lat = airport_data[iata_code]['lat']
        lon = airport_data[iata_code]['lon']
        return lat, lon
    else:
        return None, None  


