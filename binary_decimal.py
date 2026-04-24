# Binary ↔ Decimal Converter
# Converts between binary and decimal number systems

def decimal_to_binary(n):
    return bin(n)[2:]  # Remove '0b' prefix

def binary_to_decimal(b):
    return int(b, 2)

print("1. Decimal → Binary")
print("2. Binary → Decimal")
choice = input("Choose (1 or 2): ").strip()

if choice == '1':
    n = int(input("Enter a decimal number: "))
    print(f"Binary: {decimal_to_binary(n)}")
elif choice == '2':
    b = input("Enter a binary number: ")
    print(f"Decimal: {binary_to_decimal(b)}")
else:
    print("Invalid choice.")
