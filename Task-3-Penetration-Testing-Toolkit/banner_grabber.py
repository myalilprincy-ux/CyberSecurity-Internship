import socket

# Grab service banner

def grab_banner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, port))

        banner = s.recv(1024)
        print(f"Banner: {banner.decode().strip()}")

        s.close()

    except:
        print("Unable to grab banner")

# Main

ip = input("Enter IP: ")
port = int(input("Enter Port: "))

grab_banner(ip, port)