# Symmetric and Palindrome Program

string = input("Enter a string: ")

length = len(string)

# Check Symmetric
if length % 2 == 0:
    mid = length // 2
    if string[:mid] == string[mid:]:
        print("The string is Symmetric")
    else:
        print("The string is not Symmetric")
else:
    print("The string is not Symmetric")

# Check Palindrome
if string == string[::-1]:
    print("The string is a Palindrome")
else:
    print("The string is not a Palindrome")
