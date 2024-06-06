from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            #Example encryption: Swapping red and blue channels
            encrypted_pixel = (b, g, r)

            pixels[i, j] = encrypted_pixel
    
    img.save(output_path)
    print("Image Encrypted successfully!")

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # Swapping red and blue channels back
            decrypted_pixel = (b, g, r)

            pixels[i, j] = decrypted_pixel

    img.save(output_path)
    print("Image Decrypted successfully!")

#Example Usage:
input_image = r"C:\Users\path\to\input.jpeg"
encrypted_image = r"C:\Users\path\to\encrypted.jpeg"
decrypted_image = r"C:\Users\path\to\decrypted.jpeg"

# Encrypt the image
encrypt_image(input_image, encrypted_image, key= None)

#Decrypt the image
decrypt_image(encrypted_image, decrypted_image, key= None)
            
