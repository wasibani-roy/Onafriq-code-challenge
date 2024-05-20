
import requests

# Base URL of the API
base_url = "https://restful-booker.herokuapp.com"

#Login as user
def get_token(username,password):
    url = base_url + "/auth"
    data = {
        "username":username,
        "password":password
    }
    response = requests.post(url, json=data)
    return response.json()

# Function to create a booking
def create_booking(firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds):
    url = base_url + "/booking"
    data = {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": totalprice,
        "depositpaid": depositpaid,
        "bookingdates": {
            "checkin": checkin,
            "checkout": checkout
        },
        "additionalneeds": additionalneeds
    }
    response = requests.post(url, json=data)
    return response.json()

# Function to get a booking by ID
def get_booking(booking_id):
    url = base_url + f"/booking/{booking_id}"
    response = requests.get(url)
    return response.json()

# Function to update a booking
def update_booking(booking_id, checkout, additionalneeds, user_token):
    url = base_url + f"/booking/{booking_id}"
    data = {
        "bookingdates": {
            "checkout": checkout
        },
        "additionalneeds": additionalneeds
    }
    headers = {
        "Content-Type":"application/json",
        "Cookie": "token="+user_token
    }
    response = requests.patch(url, json=data, headers=headers)
    return response.json()

# Example usage
if __name__ == "__main__":
    # Get user token
    login_user = get_token("admin","password123")
    access_token = login_user['token']

    # Create a booking
    booking = create_booking("John", "Doe", 200, True, "2024-05-15", "2024-05-17", "Breakfast")

    # Get the booking created above
    booking_id = booking["bookingid"]
    print("Created booking:", booking)
    print("Booking ID:", booking_id)

    # Get the booking by ID
    retrieved_booking = get_booking(booking_id)
    print("Retrieved booking:", retrieved_booking)

    # Update the booking
    updated_booking = update_booking(booking_id, "2024-05-18", "Lunch",access_token)
    print("Updated booking:", updated_booking)