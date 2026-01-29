# def check_weather(weather):
#     if weather == "sunny":
#         return "Go for walk"
#     if weather == "rainy":
#         return "Read a book"
#     if weather == "snowy":
#         return "Build a snowman"
#     else:
#         return "❓ Unknown State"

# weather = input("Enter Weather Condition:  ").strip().lower()
# print("Result: ", check_weather(weather))


def check_weather(choice):
    if choice == 1:
        return "☀️ Sunny! Go for a walk 🚶‍♂️🌳"
    elif choice == 2:
        return "🌧️ Rainy! Read a book 📖☕"
    elif choice == 3:
        return "❄️ Snowy! Build a snowman ⛄"
    else:
        return "❓ Invalid choice! Please select 1, 2 or 3 😕"


print("🌦️ Select Weather Condition 🌦️")
print("1️⃣ Sunny ☀️")
print("2️⃣ Rainy 🌧️")
print("3️⃣ Snowy ❄️")

choice = int(input("👉 Enter your choice (1/2/3): "))

print("\nResult 👉", check_weather(choice))
