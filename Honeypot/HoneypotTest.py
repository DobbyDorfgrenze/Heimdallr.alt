import socket
import threading
import time

def handle_client(client_socket):
    print(f"[*] Accepted connection from: {client_socket.getpeername()}")
    client_socket.send(b"Welcome to the SSH honeypot!\n")
    client_socket.close()

def main():
    bind_ip = "0.0.0.0"
    bind_port = 22

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server.bind((bind_ip, bind_port))

    server.listen(5)
    print(f"[*] Listening on {bind_ip}:{bind_port}")

    while True:
        try:
            client, addr = server.accept()
            print(f"[*] Accepted connection from: {addr[0]}:{addr[1]}")

            client_handler = threading.Thread(target=handle_client, args=(client,))
            client_handler.start()
        except KeyboardInterrupt:
            print("[*] User interrupted. Exiting.")
            break

if __name__ == "__main__":
    main()

