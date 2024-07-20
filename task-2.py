from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    # Convert the image to a numpy array
    img_array = np.array(img)
    
    # Perform XOR operation on each pixel value with the key
    encrypted_array = img_array ^ key
    
    # Convert the encrypted array back to an image
    encrypted_img = Image.fromarray(encrypted_array)
    
    return encrypted_img

def decrypt_image(encrypted_img, key):
    # Convert the encrypted image to a numpy array
    encrypted_array = np.array(encrypted_img)
    
    # Perform XOR operation on each pixel value with the key to decrypt
    decrypted_array = encrypted_array ^ key
    
    # Convert the decrypted array back to an image
    decrypted_img = Image.fromarray(decrypted_array)
    
    return decrypted_img

def main():
    while True:
        choice = input("Would you like to (e)ncrypt or (d)ecrypt an image? (q to quit): ").lower()
        if choice == 'e':
            image_path = input("Enter the path of the image to encrypt: ")
            key = int(input("Enter the encryption key (integer value): "))
            encrypted_img = encrypt_image(image_path, key)
            encrypted_img.show()
            save_path = input("Enter the path to save the encrypted image (e.g., encrypted.png): ")
            encrypted_img.save(save_path)
            print(f"Encrypted image saved to {save_path}")
        elif choice == 'd':
            image_path = input("Enter the path of the encrypted image to decrypt: ")
            key = int(input("Enter the decryption key (integer value): "))
            encrypted_img = Image.open(image_path)
            decrypted_img = decrypt_image(encrypted_img, key)
            decrypted_img.show()
            save_path = input("Enter the path to save the decrypted image (e.g., decrypted.png): ")
            decrypted_img.save(save_path)
            print(f"Decrypted image saved to {save_path}")
        elif choice == 'q':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit.")

if __name__ == "__main__":
    main()
