import socket
import json

mac = "AA:BB:CC:DD:EE:FF"


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 9999))

        # Send DISCOVER
        discover = {"type": "DISCOVER", "mac": mac}
        s.send(json.dumps(discover).encode())

        # Receive OFFER
        data = s.recv(1024).decode()
        offer = json.loads(data)
        print(f"[CLIENT] Received OFFER: {offer['ip']}")

        # Send REQUEST
        request = {"type": "REQUEST", "mac": mac, "ip": offer["ip"]}
        s.send(json.dumps(request).encode())

        # Receive ACK
        ack = json.loads(s.recv(1024).decode())
        print(f"[CLIENT] Received ACK: IP assigned is {ack['ip']}")


if __name__ == "__main__":
    main()
