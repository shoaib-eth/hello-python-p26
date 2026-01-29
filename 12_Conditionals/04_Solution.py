# fruit_Color = input("Enter Fruit Color (In Lower Case Only):  ")

# if fruit_Color == "green":
#     print("Banana is Unripe")
# elif fruit_Color == "yellow":
#     print("Banana is Ripe")
# elif fruit_Color == "brown":
#     print("Banana is Overipe")
# else:
#     print("Banana is Fresh")


def check_banana(color):
    if color == "green":
        return "🟢 Unripe 😬"
    elif color == "yellow":
        return "🟡 Ripe 😋"
    elif color == "brown":
        return "🟤 Overripe 🤢"
    else:
        return "❓ Unknown state 🍌"


fruit_color = input("🍌 Enter Banana Color: ").strip().lower()
print("Result:", check_banana(fruit_color))
