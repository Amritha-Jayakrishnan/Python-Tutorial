# Investment Calculation Program

principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (%): "))
time = float(input("Enter time in years: "))

# Simple Interest
simple_interest = (principal * rate * time) / 100

# Compound Interest
compound_amount = principal * (1 + rate/100) ** time
compound_interest = compound_amount - principal

print("Simple Interest:", simple_interest)
print("Compound Interest:", compound_interest)
print("Total Amount after Compound Interest:", compound_amount)