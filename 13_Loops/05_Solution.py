input_str = input("Input a String: ")

for char in input_str:
    if input_str.count(char) == 1:
        print("Char is: ", char)
        break
