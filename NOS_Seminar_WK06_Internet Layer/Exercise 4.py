import ipaddress

# Base network
network = ipaddress.ip_network("172.16.0.0/16")

# Required sizes
departments = {
    "Engineering": 30,
    "Marketing": 15,
    "Finance": 10,
    "HR": 5
}

# Allocating subnets using /27 (32 total IPs, 30 usable)
subnets = list(network.subnets(new_prefix=27))

# Assign subnets to departments
for i, (dept, size) in enumerate(departments.items()):
    subnet = subnets[i]
    hosts = list(subnet.hosts())  # exclude network and broadcast
    print(f"{dept}:")
    print(f"  Subnet: {subnet}")
    print(f"  Usable IPs: {hosts[0]} - {hosts[-1]}\n")
