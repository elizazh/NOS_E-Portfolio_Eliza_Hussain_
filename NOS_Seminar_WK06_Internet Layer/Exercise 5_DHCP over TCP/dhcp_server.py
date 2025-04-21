import socket
import json

IP_POOL = ["192.168.1.100", "192.168.1.101", "192.168.1.102"]
LEASES = {}

def handle_client(conn):
    data = conn.recv(1024).decode()
    msg = json.loads(data)

    if msg["type"] == "DISCOVER":
        print("[SERVER] Received DISCOVER")
        offered_ip = IP_POOL.pop(0)
        response = {"type": "OFFER", "ip": offered_ip}
        conn.send(json.dumps(response).encode())

        data = conn.recv(1024).decode()
        msg = json.loads(data)
        if msg["type"] == "REQUEST":
            print("[SERVER] Received REQUEST")
            LEASES[msg["mac"]] = msg["ip"]
            ack = {"type": "ACK", "ip": msg["ip"]}
            conn.send(json.dumps(ack).encode())
            print(f"[SERVER] Leased IP {msg['ip']} to {msg['mac']}")

    conn.close()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 9999))
        s.listen()
        print("[SERVER] DHCP Server running...")
        while True:
            conn, addr = s.accept()
            handle_client(conn)

if __name__ == "__main__":
    main()
