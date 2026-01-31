# def greet(name = "Alice"): # print Alice if name was not passed
#     return "Hello 👋" + name

# input_name = input("Enter Your Name: ")
# print(greet(input_name)) # it prints the name
# print(greet())

# MORE IMPROVED VERSION


def greet(name="Alice"):
    return f"Hello 👋 {name}"


print("===================================")
print("        🙋 GREETING APP 🙋")
print("===================================")

input_name = input("👉 Enter your name (leave empty for default): ")

if input_name.strip() == "":
    print(greet())
else:
    print(greet(input_name))

print("\n✨ Have a great day! ✨")
