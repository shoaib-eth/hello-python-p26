print("📅 Leap Year Checker 📅\n")


def is_leap_year(year):
    if year % 400 == 0:
        return "🟢 Leap Year"
    elif year % 100 == 0:
        return "🔴 Not a Leap Year"
    elif year % 4 == 0:
        return "🟢 Leap Year"
    else:
        return "🔴 Not a Leap Year"


try:
    year = int(input("📥 Enter a year: "))
    print("\nResult 👉", is_leap_year(year))
except ValueError:
    print("⚠️ Please enter a valid year (numbers only).")
