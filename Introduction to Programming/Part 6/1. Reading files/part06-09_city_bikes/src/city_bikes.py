# Write your solution here
import math

def get_station_data(filename: str) -> dict:
    """Returns the name and location of all the stations in a given file as a dictionary"""
    stations = {}
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            parts = line.split(";")
            if parts[-1] == "id":
                continue
            name = parts[3]
            location = (float(parts[0]), float(parts[1]))
            stations[name] = location
    return stations


def distance(stations: dict, station1: str, station2: str) -> float:
    """Returns the distance between the two stations given"""
    longitude1, latitude1 = stations[station1]
    longitude2, latitude2 = stations[station2]
    
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    
    return distance_km


def greatest_distance(stations: dict) -> tuple:
    """Returns the two stations with the greatest distance from each other
    and the distance between the two"""
    greatest = 0
    
    # Compare with each station
    for t_station1 in stations.keys():
        for t_station2 in stations.keys():
            if t_station1 != t_station2:
                temp_distance = distance(stations, t_station1, t_station2)
                if greatest < temp_distance:
                    greatest = temp_distance
                    station1 = t_station1
                    station2 = t_station2
    return station1, station2, greatest
    


if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)
    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)
    
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)