# order_size = input("Enter Your Coffee Order Size: ").strip().lower()
# extra_shot = True

# if extra_shot:
#     coffee =  order_size + " Coffee with an extra shot"
# else:
#     coffee = order_size + " Coffee"

# print("Order: ", coffee)

print("☕ Welcome to Python Café ☕\n")

# Coffee size input
order_size = input("📏 Choose coffee size (Small / Medium / Large): ").strip().lower()

# Extra shot choice
extra_shot_input = (
    input("⚡ Would you like an extra shot of espresso? (yes/no): ").strip().lower()
)

# Convert yes/no to boolean
extra_shot = extra_shot_input == "yes"

# Validate size
if order_size not in ["small", "medium", "large"]:
    print("❌ Invalid coffee size selected.")
else:
    coffee = order_size.capitalize() + " Coffee"

    if extra_shot:
        coffee += " with an extra shot ☕⚡"
    else:
        coffee += " ☕"

    print("\n✅ Order Confirmed!")
    print("🧾 Order:", coffee)
