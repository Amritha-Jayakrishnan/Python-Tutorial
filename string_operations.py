# String Operations
# Demonstrates common string manipulations in Python

text = input("Enter a string: ")

print("\n--- String Operations ---")
print(f"Original    : {text}")
print(f"Uppercase   : {text.upper()}")
print(f"Lowercase   : {text.lower()}")
print(f"Reversed    : {text[::-1]}")
print(f"Length      : {len(text)}")
print(f"Word count  : {len(text.split())}")
print(f"Capitalized : {text.capitalize()}")
print(f"Title case  : {text.title()}")
print(f"Stripped    : '{text.strip()}'")
print(f"Replace 'a' with '@': {text.replace('a', '@')}")
