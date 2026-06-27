def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


# Main Program
print("Caesar Cipher")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Enter your choice (1/2): ")

message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

if choice == "1":
    encrypted = encrypt(message, shift)
    print("Encrypted Message:", encrypted)

elif choice == "2":
    decrypted = decrypt(message, shift)
    print("Decrypted Message:", decrypted)

else:
    print("Invalid choice!")