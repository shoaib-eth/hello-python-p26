def multiply(a, b):
    return a * b


print("===================================")
print("      ✨ MULTIPLICATION APP ✨")
print("===================================")

# Integer Multiplication
print("\n🔢 Integer Multiplication")
num1 = int(input("👉 Enter 1st Number: "))
num2 = int(input("👉 Enter 2nd Number: "))

print(f"\n✅ Result: {num1} × {num2} = {multiply(num1, num2)}")

# String Multiplication
print("\n-----------------------------------")
print("🔤 String Multiplication")

count = int(input("👉 Enter repeat count: "))
text = input("👉 Enter a String: ")

print("\n📢 Result:")
print(multiply(count, text))

print("\n✨ Thank you for using the app ✨")
