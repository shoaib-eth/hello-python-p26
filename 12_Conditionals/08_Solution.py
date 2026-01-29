"""
print("🔐 Password Strength Checker 🔐\n")

def check_password(password):
    length = len(password)

    if length < 6:
        return "🔴 Weak password"
    elif length <= 10:
        return "🟡 Medium password"
    else:
        return "🟢 Strong password 💪"

password = input("🔑 Enter your password: ")

print("\nResult 👉", check_password(password))
"""

# Using getpass for hide the password in terminal during password entering

import getpass

print("🔐 Password Strength Checker 🔐\n")


def check_password(password):
    length = len(password)

    if length < 6:
        return "🔴 Weak password"
    elif length <= 10:
        return "🟡 Medium password"
    else:
        return "🟢 Strong password 💪"


# Password input (hidden)
password = getpass.getpass("🔑 Enter your password: ")

print("\nResult 👉", check_password(password))
