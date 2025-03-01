from PIL import Image
import random
import os

#to make sure that the input has .format extentions
VALID_EXTENSIONS = ['.png', '.jpg', '.jpeg']

def add_default_extension(output_path):
    if not any(output_path.lower().endswith(ext) for ext in VALID_EXTENSIONS):
        output_path += '.png'
    return output_path

def encrypt_image(image_path, output_path, key):
    # Check if image file exists
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"No such file: '{image_path}'")
    # Check for valid output extension
    output_path = add_default_extension(output_path)

    # Open the image
    image = Image.open(image_path)
    pixels = image.load()

    # Get image dimensions
    width, height = image.size

    # Seed the random number generator with the key
    random.seed(key)

    # Encrypt the image by swapping and altering pixel values
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x,y]
            # Swap the red and blue values
            r, b = b, r
            # Apply a basic mathematical operation
            r = (r + random.randint(0, 255)) % 256
            g = (g + random.randint(0, 255)) % 256
            b = (b + random.randint(0, 255)) % 256
            pixels[x, y] = (r, g, b)
    # Save the encrypted image
    image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

#DEcrypt function
def decrypt_image(image_path, output_path, key):
    #opens image, loads pixels, get dimension, seeds the random number with key
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size
    random.seed(key)
    #loops through pixels and get pixel values
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            #reverses altered pixel values
            r = (r - random.randint(0, 255)) % 256
            g = (g - random.randint(0, 255)) % 256
            b = (b - random.randint(0, 255)) % 256
            r, b = b, r
            pixels[x, y] = (r, g, b)
    image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

#the main function and input
def main():
    while True:
        action = input("Do you want to (E)ncrypt or (D)ecrypt and (Q) to quit: ").upper()
        if action == 'Q':
            print("Thanks for using lazy hunter's image encrypt tool")
            break
        elif action not in ['E', 'D']:
            print("Please enter either E to encrypt or D to decrypt or Q to quit ")
            continue

        image_path = input("Enter the path to the image file: ")
        output_path = input("Enter the path to save the output image: ")
        key = input("Enter the encryption/decryption key: ")

        if action == 'E':
            encrypt_image(image_path, output_path, key)
        elif action == 'D':
            decrypt_image(image_path, output_path, key)

if __name__ == "__main__":
    main()





