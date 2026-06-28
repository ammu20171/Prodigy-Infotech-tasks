from PIL import Image

# Encrypt Image
def encrypt_image(input_image, output_image, key):
    img = Image.open(input_image)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256

            pixels[x, y] = (r, g, b)

    img.save(output_image)
    import os

    img.save(output_image)
    print("Saved at:", os.path.abspath(output_image))
    print("Encrypted image saved as:", output_image)


# Decrypt Image
def decrypt_image(input_image, output_image, key):
    img = Image.open(input_image)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256

            pixels[x, y] = (r, g, b)

    img.save(output_image)
    import os


    img.save(output_image)
    print("Saved at:", os.path.abspath(output_image))
    print("Decrypted image saved as:", output_image)


# Main Program
print("Image Encryption Tool")
print("1. Encrypt Image")
print("2. Decrypt Image")

choice = input("Enter your choice (1/2): ")

input_image = input("Enter input image filename: ")
output_image = input("Enter output image filename: ")
key = int(input("Enter encryption key (0-255): "))

if choice == "1":
    encrypt_image(input_image, output_image, key)
elif choice == "2":
    decrypt_image(input_image, output_image, key)
else:
    print("Invalid choice!")