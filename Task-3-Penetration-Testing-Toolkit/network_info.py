import socket

# Get hostname

def get_host_info(hostname):
    try:
        ip = socket.gethostbyname(hostname)
        print(f"Hostname: {hostname}")
        print(f"IP Address: {ip}")

    except socket.error:
        print("Unable to resolve hostname")

# Main

host = input("Enter hostname: ")
get_host_info(host)