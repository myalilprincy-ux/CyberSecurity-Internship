import hashlib
import json
import os

HASH_DB = "hashes.json"

# Generate SHA-256 hash

def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    try:
        with open(file_path, 'rb') as file:
            while chunk := file.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()

    except FileNotFoundError:
        return None

# Load stored hashes

def load_hashes():
    if os.path.exists(HASH_DB):
        with open(HASH_DB, 'r') as file:
            return json.load(file)
    return {}

# Save hashes

def save_hashes(hashes):
    with open(HASH_DB, 'w') as file:
        json.dump(hashes, file, indent=4)

# Add new file

def add_file(file_path):
    hashes = load_hashes()
    file_hash = calculate_hash(file_path)

    if file_hash:
        hashes[file_path] = file_hash
        save_hashes(hashes)
        print(f"[+] File added successfully: {file_path}")
    else:
        print("[-] File not found")

# Check integrity

def check_integrity():
    hashes = load_hashes()

    for file_path, old_hash in hashes.items():
        current_hash = calculate_hash(file_path)

        if current_hash is None:
            print(f"[-] File missing: {file_path}")

        elif current_hash == old_hash:
            print(f"[OK] No changes detected: {file_path}")

        else:
            print(f"[WARNING] File modified: {file_path}")

# Menu

def main():
    while True:
        print("\nFILE INTEGRITY CHECKER")
        print("1. Add File")
        print("2. Check Integrity")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            path = input("Enter file path: ")
            add_file(path)

        elif choice == '2':
            check_integrity()

        elif choice == '3':
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()