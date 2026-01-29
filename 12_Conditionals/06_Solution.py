# print("Mode of Transportation")

# def check_distance(distance):
#     if distance <= 3:
#         return "Walk"
#     elif distance <= 15:
#         return "Bike"
#     else:
#         return "Car"

# distance = int(input("Enter Distance in Km:  "))
# print("Mode of Transportation should be ", check_distance(distance))

#  More Interactive Version 👇🏻

print("🚦 Transportation Mode Finder 🚦\n")


def check_distance(distance):
    if distance <= 0:
        return "❌ Distance must be greater than zero."
    elif distance <= 3:
        return "🚶 Walk – Best for short distances."
    elif distance <= 15:
        return "🚴 Bike – Fast and economical."
    else:
        return "🚗 Car – Comfortable for long distances."


try:
    distance = float(input("📍 Enter distance in kilometers: ").strip())
    print("\n👉 Recommended mode:", check_distance(distance))
except ValueError:
    print("⚠️ Please enter a valid number (e.g., 2, 5.5, 10).")
