import socket
import threading
import pickle
import rsa

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    publicKey, privateKey = rsa.newkeys(512)
    with open('Public-Key.txt', 'wb') as f:
        pickle.dump(publicKey, f)

    
    server_address = ('localhost', 9999)
    server_socket.bind(server_address)

    server_socket.listen(5)
    print('Server started. Listening for incoming connections...')

    while True:
        try:
            client_socket, client_address = server_socket.accept()
            print(f'Incoming connection from: {client_address}')
            client_socket.setblocking(False)


            client_handler = threading.Thread(target = client_Handler, args=(client_socket,))
            client_handler.start()
        except KeyboardInterrupt:
            print("[*] User interrupted. Exiting...")
            break


def client_Handler(client_socket):
    #client_socket.send("ready".encode())
    request = pickle.loads(client_socket.recv(2048))
    #request = client_socket.recv(2048).decode()
    print("Received ")
    print(request)
    print(" from Client")
    # hier Logik einbauen
    # was genau soll der server eigentlich können?
    


    client_socket.close()
    print("Connection closed")

if __name__ == '__main__':
    start_server()

#gorila and gin frameworks for go
#marshall and unmarshall for json files
#