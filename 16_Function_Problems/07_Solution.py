# def sum_all(*args):
#     result = sum(args)
#     return result

# a, b, c, d, e = map(int, input("Enter Five Numbers (Take Spaces b/w Them): ").split())
# print(f"The Sum of {a} + {b} + {c} + {d} + {e} is ", sum_all(a, b, c, d, e))

# MORE INVESTIGTIONS 
def sum_all(*args):
    print(args)
    for i in args:
        print(i * 2)

a, b, c, d, e = map(int, input("Enter Five Numbers (Take Spaces b/w Them): ").split())
sum_all(a, b, c, d, e)