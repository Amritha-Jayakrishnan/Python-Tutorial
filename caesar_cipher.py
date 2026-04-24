# Caesar Cipher
# Encrypts and decrypts text by shifting letters by a given key

def caesar_cipher(text, shift, mode='encrypt'):
    if mode == 'decrypt':
        shift = -shift
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

text = input("Enter text: ")
shift = int(input("Enter shift key (e.g. 3): "))
mode = input("Encrypt or Decrypt? (e/d): ").strip().lower()
mode = 'decrypt' if mode == 'd' else 'encrypt'

output = caesar_cipher(text, shift, mode)
print(f"Result: {output}")
