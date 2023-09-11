import socket

def start_server():
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific IP address and port
    server_address = ('localhost', 9999)
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)
    print('Server started. Listening for incoming connections...')

    while True:
        # Accept a client connection
        client_socket, client_address = server_socket.accept()
        print(f'Incoming connection from: {client_address}')

        # Receive and process data from the client
        data = client_socket.recv(1024).decode()
        print(f'Received data from client: {data}')

        # Send a response back to the client
        response = 'Server received the message successfully'
        client_socket.send(response.encode())

        # Close the client connection
        client_socket.close()

if __name__ == '__main__':
    start_server()

#gorila and gin frameworks for go
#marshall and unmarshall for json files
#