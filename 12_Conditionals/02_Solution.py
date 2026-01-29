from datetime import datetime

# User se age input
age = int(input("Enter Your Age: "))

# Fetch the day
day = datetime.now().strftime("%A")  # e.g. Monday, Tuesday, Wednesday

# Base price
price = 12 if age >= 18 else 8

# Sunday discount
if day == "Sunday":
    price -= 2

print("Today is:", day)
print("Ticket Price For You Is $", price)
