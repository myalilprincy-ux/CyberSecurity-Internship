from cryptography.fernet import Fernet

key = Fernet.generate_key()

cipher = Fernet(key)

message = input("Enter message: ").encode()

encrypted = cipher.encrypt(message)

print("Encrypted:", encrypted)

decrypted = cipher.decrypt(encrypted)

print("Decrypted:", decrypted.decode())