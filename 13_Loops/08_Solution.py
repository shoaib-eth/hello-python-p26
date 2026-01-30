input_num = int(input("Enter a Number:  "))

is_prime = True

if input_num > 1:
    for i in range(2, input_num):
        if (input_num % i) == 0:
            is_prime = False
            break

print(is_prime)
