def calculate_sum(num1, num2):
    result = num1 + num2
    return result


input_num1 = int(input("Enter First Number  : "))
input_num2 = int(input("Enter Second Number : "))
print(
    f"The Sum of {input_num1} and {input_num2} is ",
    calculate_sum(input_num1, input_num2),
)


# Another methods we can use
# a, b = map(int, input("Enter two numbers (Take Space b/w Both): ").split())
# print(f"Sum of {a} + {b} is ", calculate_sum(a, b))
