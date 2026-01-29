print("🐾 Pet Food Recommendation System 🐾\n")


def recommend_food(species, age):
    if age <= 0:
        return "❌ Age must be greater than zero."

    if species == "dog":
        if age <= 2:
            return "🐶 Puppy Food – Supports growth and energy."
        elif age <= 7:
            return "🐕 Adult Dog Food – Balanced nutrition."
        else:
            return "🐕‍🦺 Senior Dog Food – Easy to digest."

    elif species == "cat":
        if age <= 2:
            return "🐱 Kitten Food – High protein for growth."
        elif age <= 5:
            return "🐈 Adult Cat Food – Maintains health."
        else:
            return "🐈‍⬛ Senior Cat Food – Supports joints and digestion."

    else:
        return "❓ Unknown pet species."


# User input
species = input("🐾 Enter pet species (dog / cat): ").strip().lower()

try:
    age = float(input("📅 Enter pet age (in years): ").strip())
    print("\n👉 Recommendation:", recommend_food(species, age))
except ValueError:
    print("⚠️ Please enter a valid age (numbers only).")
