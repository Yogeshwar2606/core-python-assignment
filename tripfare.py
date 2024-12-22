def calculate_fare(distance):
    base_fare = 50
    distance_fare = 10
    total_fare = base_fare + (distance * distance_fare)
    return total_fare
def calculate_total_fare(trips):
    total_fare = 0
    for i, trip in enumerate(trips, start=1):
        trip_fare = calculate_fare(trip)
        print(f"Trip {i}: ${trip_fare}")
        total_fare += trip_fare
    return total_fare
trips = [5, 10, 3]
total_fare = calculate_total_fare(trips)
print(f"Total Fare: ${total_fare}")