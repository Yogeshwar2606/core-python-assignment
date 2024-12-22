def book_seat(total_seats, booked_seats, seat):
    if seat > total_seats or seat < 1:
        return f"Seat {seat} is not valid."
    if seat in booked_seats:
        return f"Seat {seat} is already booked."
    else:
        booked_seats.append(seat)
        booked_seats.sort()  
        return f"Seat {seat} has been successfully booked."
def cancel_seat(booked_seats, seat):
    if seat not in booked_seats:
        return f"Seat {seat} was not booked."
    else:
        booked_seats.remove(seat)
        return f"Seat {seat} has been successfully canceled."
def available_seats(total_seats, booked_seats):
    return [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]
total_seats = 10
booked_seats = [2, 5, 7]
book_seat_number = 3
cancel_seat_number = 5
print("Available seats:",available_seats(total_seats, booked_seats))
