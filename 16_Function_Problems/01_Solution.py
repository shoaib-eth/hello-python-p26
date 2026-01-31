def calculate_square(number):
    # result = number * number
    result = number**2
    return result


number = int(input("Enter a Number:  "))
print(f"Square of {number} is ", calculate_square(number))
