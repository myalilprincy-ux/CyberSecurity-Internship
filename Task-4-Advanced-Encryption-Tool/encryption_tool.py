from cryptography.fernet import Fernet
import os

# Generate key

def generate_key():
    key = Fernet.generate_key()

    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load key

def load_key():
    return open("secret.key", "rb").read()

# Encrypt file

def encrypt_file(filename, key):
    f = Fernet(key)

    with open(filename, "rb") as file:
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    with open(filename, "wb") as file:
        file.write(encrypted_data)

    print("[+] File encrypted successfully")

# Decrypt file

def decrypt_file(filename, key):
    f = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    with open(filename, "wb") as file:
        file.write(decrypted_data)

    print("[+] File decrypted successfully")

# Main

def main():
    if not os.path.exists("secret.key"):
        generate_key()

    key = load_key()

    print("1. Encrypt File")
    print("2. Decrypt File")

    choice = input("Enter choice: ")
    filename = input("Enter file name: ")

    if choice == '1':
        encrypt_file(filename, key)

    elif choice == '2':
        decrypt_file(filename, key)

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()