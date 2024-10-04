def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result
def main():
    print("Welcome to Caesar Cipher Program")
    text = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    encrypted_text = caesar_cipher(text, shift, mode='encrypt')
    print(f"Encrypted Message: {encrypted_text}")
    decrypted_text = caesar_cipher(encrypted_text, shift, mode='decrypt')
    print(f"Decrypted Message: {decrypted_text}")
if __name__ == "__main__":
    main()
