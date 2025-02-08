
'''
1. Add flights to the system.

2. Search for flights by destination.

3. Book a seat on a flight.

4. Cancel a booking.

5. View all flights and their available seats.

6. View all bookings for a specific flight.

7.Calculate the total revenue from all bookings.
'''





# Global variables to store flight and booking data
flights = {}  # Dictionary to store flights and their details
bookings = {}  # Dictionary to store bookings

# Function to add a flight
def add_flight(flight_id, destination, total_seats):
    if flight_id in flights:
        print(f"Flight with ID {flight_id} already exists.")
    else:
        flights[flight_id] = {
            "destination": destination,
            "total_seats": total_seats,
            "available_seats": total_seats,
            "bookings": []  # List to store bookings for this flight
        }
        print(f"Flight {flight_id} to {destination} with {total_seats} seats added to the system.")

# Function to search for flights by destination
def search_flights(destination):
    results = []
    for flight_id, flight in flights.items():
        if flight["destination"].lower() == destination.lower():
            results.append(flight_id)
    return results

# Function to book a seat on a flight
def book_seat(flight_id, passenger_name):
    if flight_id not in flights:
        print(f"Flight with ID {flight_id} does not exist.")
        return
    if flights[flight_id]["available_seats"] <= 0:
        print(f"No available seats on flight {flight_id}.")
        return
    booking_id = f"{flight_id}_{passenger_name}"
    if booking_id in bookings:
        print(f"Passenger {passenger_name} already has a booking on flight {flight_id}.")
        return
    flights[flight_id]["available_seats"] -= 1
    flights[flight_id]["bookings"].append(booking_id)
    bookings[booking_id] = {
        "flight_id": flight_id,
        "passenger_name": passenger_name,
        "status": "Booked"
    }
    print(f"Seat booked for {passenger_name} on flight {flight_id}.")

# Function to cancel a booking
def cancel_booking(booking_id):
    if booking_id not in bookings:
        print(f"Booking with ID {booking_id} does not exist.")
        return
    flight_id = bookings[booking_id]["flight_id"]
    flights[flight_id]["available_seats"] += 1
    flights[flight_id]["bookings"].remove(booking_id)
    del bookings[booking_id]
    print(f"Booking {booking_id} canceled successfully.")

# Function to view all flights and their available seats
def view_all_flights():
    if not flights:
        print("No flights in the system.")
    else:
        print("\nAll Flights and Available Seats:")
        for flight_id, flight in flights.items():
            print(f"Flight ID: {flight_id}, Destination: {flight['destination']}, Available Seats: {flight['available_seats']}/{flight['total_seats']}")

# Function to view all bookings for a specific flight
def view_bookings_for_flight(flight_id):
    if flight_id not in flights:
        print(f"Flight with ID {flight_id} does not exist.")
        return
    if not flights[flight_id]["bookings"]:
        print(f"No bookings for flight {flight_id}.")
    else:
        print(f"\nBookings for Flight {flight_id}:")
        for booking_id in flights[flight_id]["bookings"]:
            print(f"Booking ID: {booking_id}, Passenger: {bookings[booking_id]['passenger_name']}, Status: {bookings[booking_id]['status']}")

# Function to calculate the total revenue from all bookings
def calculate_total_revenue(price_per_seat):
    total_revenue = 0
    for booking_id in bookings:
        total_revenue += price_per_seat
    print(f"Total revenue from all bookings: ${total_revenue:.2f}")

# Main function to interact with the user
def __main__():
    while True:
        print("\nWelcome to the Flight Booking System!")
        print("1. Add Flight")
        print("2. Search Flights")
        print("3. Book Seat")
        print("4. Cancel Booking")
        print("5. View All Flights")
        print("6. View Bookings for a Flight")
        print("7. Calculate Total Revenue")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            flight_id = input("Enter flight ID: ")
            destination = input("Enter destination: ")
            total_seats = int(input("Enter total seats: "))
            add_flight(flight_id, destination, total_seats)

        elif choice == "2":
            destination = input("Enter destination to search: ")
            results = search_flights(destination)
            if results:
                print("\nSearch Results:")
                for flight_id in results:
                    print(f"Flight ID: {flight_id}, Destination: {flights[flight_id]['destination']}, Available Seats: {flights[flight_id]['available_seats']}/{flights[flight_id]['total_seats']}")
            else:
                print("No flights found for the given destination.")

        elif choice == "3":
            flight_id = input("Enter flight ID: ")
            passenger_name = input("Enter passenger name: ")
            book_seat(flight_id, passenger_name)

        elif choice == "4":
            booking_id = input("Enter booking ID: ")
            cancel_booking(booking_id)

        elif choice == "5":
            view_all_flights()

        elif choice == "6":
            flight_id = input("Enter flight ID: ")
            view_bookings_for_flight(flight_id)

        elif choice == "7":
            price_per_seat = float(input("Enter price per seat: "))
            calculate_total_revenue(price_per_seat)

        elif choice == "8":
            print("Thank you for using the Flight Booking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")