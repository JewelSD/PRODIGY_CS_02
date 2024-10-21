from PIL import Image

# Function to encrypt the image
def encrypt_image(image, shift_value):
    pixels = image.load()
    width, height = image.size

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            # Encrypt by shifting RGB values
            encrypted_r = (r + shift_value) % 256
            encrypted_g = (g + shift_value) % 256
            encrypted_b = (b + shift_value) % 256

            pixels[x, y] = (encrypted_r, encrypted_g, encrypted_b)

    return image

# Function to decrypt the image
def decrypt_image(image, shift_value):
    pixels = image.load()
    width, height = image.size

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            # Decrypt by reversing the shift
            decrypted_r = (r - shift_value) % 256
            decrypted_g = (g - shift_value) % 256
            decrypted_b = (b - shift_value) % 256

            pixels[x, y] = (decrypted_r, decrypted_g, decrypted_b)

    return image

# Main function
def main():
    # Ask the user to input the image file path
    image_path = input("Enter the path to your image file (e.g., 'your_image.jpg'): ")

    try:
        # Load the image
        image = Image.open(image_path)
    except FileNotFoundError:
        print("Error: Image file not found. Please check the path and try again.")
        return

    # Ask the user whether to encrypt or decrypt
    choice = input("Do you want to encrypt or decrypt the image? (e/d): ").lower()

    # Ask for the shift value (a number used for encryption and decryption)
    shift_value = int(input("Enter the shift value (e.g., 50): "))

    if choice == 'e':
        # Encrypt the image
        encrypted_image = encrypt_image(image.copy(), shift_value)
        encrypted_image.save("encrypted_image.png")  # Save the encrypted image
        print("Image encrypted and saved as 'encrypted_image.png'")
    elif choice == 'd':
        # Decrypt the image
        decrypted_image = decrypt_image(image.copy(), shift_value)
        decrypted_image.save("decrypted_image.png")  # Save the decrypted image
        print("Image decrypted and saved as 'decrypted_image.png'")
    else:
        print("Invalid choice. Please select 'e' for encryption or 'd' for decryption.")

# Run the main function
if __name__ == "__main__":
    main()
