import socket
import ipaddress


hostname = 'gold.ac.uk'
try:
    ip = socket.gethostbyname(hostname)
    ip_addr = ipaddress.ip_address(ip)
    print(f"IP address of {hostname}: {ip}")
    print("Is Private:", ip_addr.is_private)
    print("Is Global:", ip_addr.is_global)
except socket.gaierror as e:
    print(f"Error resolving hostname: {e}")

