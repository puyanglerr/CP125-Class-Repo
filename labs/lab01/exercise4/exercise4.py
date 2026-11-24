# Lab 01 Exercise 4: Dynamic Parking Rate
def get_hourly_rate(vehicle_type, hour):
    if vehicle_type == "Electric":
        return 2.0
    elif vehicle_type == "Hybrid":
        return 5.0 or 2.0
    else:
        return 5.0
    