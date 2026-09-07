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



if __name__ == "__main__":
    plane_name = input("Enter the name of the plane: ").strip().upper()
    if plane_name in plane_data:
        speed, range = get_plane_info(plane_name)
        print(f"Plane: {plane_name}")
        print(f"Speed: {speed} km/h")
        print(f"Range: {range} km")