import socket

target = input("Enter IP Address: ")

for port in range(1, 100):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is open")

    sock.close()