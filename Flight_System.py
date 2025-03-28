# Program to navigate a flight system for a week
name = input("Please enter your name: ")
user_id = int(input("Please enter user ID: "))

# Accepting user's name 
print(f"Hello there {name}, welcome to AirMark")

# Main Menu
print("Please select an option:")
print("1: Book a flight")
print("2: Reschedule flight")
print("3: Cancel flight")
print("4: Complaint")

# Accepting user's choice/option
tchoice = int(input(f"What's your option {name}? "))

# BOOKING A FLIGHT
if tchoice == 1:
    print("Please select route:")
    routes = [
        "PH to ABJ", "ABJ to PH", "LAGOS to ABJ", "ABJ to LAGOS", 
        "ABJ to KANO", "KANO to ABJ", "ABJ to OWERRI", "OWERRI to ABJ", 
        "ANA to ABJ", "ABJ to ANA"
    ]
    for route in routes:
        print(route)
    
    # Ensuring a valid route selection
    while True:
        route = input("Please select a route: ")
        if route in routes:
            print(f"{route} successfully selected")
            break
        else:
            print("Invalid route selection, please try again.")
    
    # Accepting flight date
    print("Please select flight date:")
    valid_dates = ["sunday", "monday", "wednesday", "thursday", "friday"]
    while True:
        flight_date = input("Please select flight date: ").lower()
        if flight_date in valid_dates:
            print("Date successfully selected")
            break
        elif flight_date == "tuesday":
            print("No running flights. Please select another day.")
        elif flight_date == "saturday":
            print("Seats have been booked out, please select another day.")
        else:
            print("Invalid date selection, please try again.")
    
    # Selecting Seats
    taken_seats = {2, 78, 43, 55, 145, 23, 77, 12, 89, 26, 22, 97, 34, 21, 98, 112, 109, 111, 76}
    while True:
        try:
            seat = int(input("Please select seat: "))
            if 1 <= seat <= 137:
                if seat in taken_seats:
                    print(f"{seat} has been taken, please select another seat")
                else:
                    print("Seat selection is successful")
                    break
            else:
                print("Invalid input, please enter a seat number between 1 and 137")
        except ValueError:
            print("Invalid input, please enter a valid number")
    
    # Baggage 
    while True:
        try:
            baggage_weight = int(input("Please enter your baggage weight: "))
            if baggage_weight > 15:
                print("You will be charged for additional weight")
            break
        except ValueError:
            print("Invalid input, please enter a numeric value.")
    
    print(f"{name}, your flight has been booked successfully")
    print(f"Your flight has been scheduled for {flight_date} and your seat number is {seat}")
    print("Thank you for choosing MarkAir")

# RESCHEDULING A FLIGHT
elif tchoice == 2:
    print("Please select reschedule reason:")
    print(f"{name}, your flight has been rescheduled successfully!")
    print("Thank you for choosing MarkAir, please fly with us again")

# CANCEL FLIGHT
elif tchoice == 3:
    print("Please select reason for flight cancellation:")
    print(f"{name}, your flight has been cancelled")
    print("Thank you for choosing MarkAir, please fly with us again")

# COMPLAINT
elif tchoice == 4:
    complaint = input("Please enter your complaint: ")
    print("Thank you for your feedback! We will address your concern promptly.")
else:
    print("Invalid option selected. Please try again.")
