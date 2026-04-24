# Square Root Program

num = float(input("Enter a number: "))

if num < 0:
    print("Square root does not exist for negative numbers")
else:
    sqrt = num ** 0.5
    print("Square root of", num, "is", sqrt)