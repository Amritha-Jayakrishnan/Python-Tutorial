# Armstrong Number
# A number is Armstrong if sum of its digits raised to the power of digit count equals itself
# Example: 153 = 1^3 + 5^3 + 3^3

def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(d) ** power for d in digits)

n = int(input("Enter a number: "))
if is_armstrong(n):
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is NOT an Armstrong number.")
