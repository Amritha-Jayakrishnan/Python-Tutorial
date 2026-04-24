TAX_RATE = float(input("Enter the tax rate (e.g., 0.2 for 20%): "))
STANDARD_DEDUCTION = float(input("Enter the standard deduction amount: "))
DEPENDENT_DEDUCTION = float(input("Enter the dependent deduction amount: "))

grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))


taxableIncome = grossIncome - STANDARD_DEDUCTION - (DEPENDENT_DEDUCTION * numDependents)


if taxableIncome < 0:
    taxableIncome = 0

incomeTax = taxableIncome * TAX_RATE


print("Taxable Income: $", round(taxableIncome, 2))
print("Income Tax to be Paid: $", round(incomeTax, 2))