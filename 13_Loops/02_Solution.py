number = int(input("Enter a Number:  "))

sum_even = 0

for num in range(1, number + 1):
    if num % 2 == 0:
        sum_even += 1

print("Sum of Even NUmber is: ", sum_even)
