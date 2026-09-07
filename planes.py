import csv
with open('planes.csv', 'r') as file:
    reader = csv.DictReader(file)
    plane_data = {row['name']: {'speed': float(row['speed']), 'range': float(row['range'])}  for row in reader}




def get_plane_info(plane_name):
    if plane_name in plane_data:
        speed = plane_data[plane_name]['speed']
        range = plane_data[plane_name]['range']
        return speed, range
    else:
        return None 



