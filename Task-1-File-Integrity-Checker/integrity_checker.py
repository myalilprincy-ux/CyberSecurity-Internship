import hashlib

def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()

file_name = input("Enter file name: ")

try:
    hash_value = calculate_hash(file_name)

    print("\nSHA-256 Hash:")
    print(hash_value)

except FileNotFoundError:
    print("File not found")