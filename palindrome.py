# Palindrome Checker
# Checks if a string or number reads the same forwards and backwards

def is_palindrome(value):
    s = str(value)
    return s == s[::-1]

user_input = input("Enter a word or number: ")
if is_palindrome(user_input):
    print(f'"{user_input}" is a Palindrome.')
else:
    print(f'"{user_input}" is NOT a Palindrome.')
