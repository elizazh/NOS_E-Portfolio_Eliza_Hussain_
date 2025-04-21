import ipaddress
import socket


def analyse_ip(ip_cidr):
    # Creating an IP interface object
    interface = ipaddress.ip_interface(ip_cidr)
    network = interface.network
    ip = interface.ip

    print(f"\nAnalyzing: {ip_cidr}")
    print(f"IP Address        : {ip}")
    print(f"Network           : {network}")
    print(f"Netmask           : {interface.netmask}")
    print(f"Broadcast Address : {network.broadcast_address}")
    print(f"Is Private        : {ip.is_private}")
    print(f"Is Global         : {ip.is_global}")

    # Usable host info
    num_hosts = network.num_addresses
    usable_hosts = num_hosts - 2 if num_hosts > 2 else 0
    print(f"Number of hosts   : {num_hosts}")
    print(f"Usable Hosts      : {usable_hosts}")

    hosts = list(network.hosts())
    if usable_hosts > 0:
        print(f"First Usable Host : {hosts[0]}")
        print(f"Last Usable Host  : {hosts[-1]}")
    else:
        print("No usable hosts in this network.")

    if num_hosts <= 256:
        print("\nAll hosts in network:")
        for h in hosts:
            print(h)



cidr_list = ['192.168.1.1/24', '192.168.1.1/30', '10.0.0.1/16']
for cidr in cidr_list:
    analyse_ip(cidr)

# Get device IP
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

print("\nYour Computer Info:")
print("Computer Name  :", hostname)
print("IP Address     :", IPAddr)
