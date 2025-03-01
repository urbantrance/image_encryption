Image Encryption Tool
Overview
This project is a simple image encryption tool that uses pixel manipulation to encrypt and decrypt images. It allows users to perform operations like swapping pixel values and applying basic mathematical operations to each pixel. The tool is designed to help secure images by making them unrecognizable until decrypted with the correct key.

Features
Encrypt Images: Encrypts images by altering pixel values and swapping colors.

Decrypt Images: Decrypts images by reversing the alterations and swaps, restoring the original image.

User Input: Prompts users to input the image file paths and encryption/decryption key interactively.

Prerequisites
Python 3.x

Pillow library (for image processing)


Installation
Clone the Repository:

sh
git clone https://github.com/yourusername/image-encryption-tool.git
cd image-encryption-tool
Create a Virtual Environment (optional but recommended):

sh
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install the Required Libraries:

sh
pip install pillow

How It Works
Encryption Process
Open Image: The script opens the image file specified by the user.

Pixel Manipulation:

Each pixel's red and blue values are swapped.

Random values are added to each RGB component, based on the encryption key.

Save Encrypted Image: The modified image is saved to the specified output path.

Decryption Process
Open Image: The script opens the encrypted image file.

Reverse Pixel Manipulation:

Random values are subtracted from each RGB component using the same key.

The red and blue values are swapped back to their original positions.

Save Decrypted Image: The restored image is saved to the specified output path.

Important Notes
The encryption/decryption key must be the same for both processes to ensure accurate decryption.

The output file path must include a valid image file extension (.png, .jpg, .jpeg).

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
The Pillow library for image processing.

The Python community for continuous support and development.
