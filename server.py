import socket
import threading

def start_server():
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

    # Bind the socket to a specific IP address and port
    server_address = ('localhost', 9999)
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(5)
    print('Server started. Listening for incoming connections...')

    while True:
        # Accept a client connection
        client_socket, client_address = server_socket.accept()
        print(f'Incoming connection from: {client_address}')

        client_handler = threading.Thread(target = client_Handler, args=(client_socket,))
        client_handler.start()


def client_Handler(client_socket):
    # send a message to the client
    client_socket.send("ready".encode())
    # receive and display a message from the client
    request = client_socket.recv(1024).decode()
    print("Received \"" + request + "\" from client")
    # close the connection again
    client_socket.close()
    print("Connection closed")

if __name__ == '__main__':
    start_server()

#gorila and gin frameworks for go
#marshall and unmarshall for json files
#