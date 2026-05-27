import socket

# Scan ports

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] Port {port}")

        sock.close()

    except Exception as e:
        print(f"Error: {e}")

# Main

def main():
    target = input("Enter target IP: ")

    for port in range(1, 1025):
        scan_port(target, port)

if __name__ == "__main__":
    main()