import socket
import threading
import pickle
import rsa
import os.path
from flask import Flask, render_template, jsonify
import sys
sys.path.insert(1, '/VulnerabilityScanner')
import Client as VS

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    publicKey, privateKey = rsa.newkeys(2048)
    with open(os.path.dirname(__file__) +'/../Public-Key.txt', 'wb') as f:
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


            client_handler = threading.Thread(target = client_Handler, args=(client_socket, privateKey,))
            client_handler.start()
        except KeyboardInterrupt:
            print("[*] User interrupted. Exiting...")
            break


def client_Handler(client_socket, privateKey):
    #client_socket.send("ready".encode())
    decMessage = rsa.decrypt(client_socket.recv(2048), privateKey)
    request = pickle.loads(decMessage)
    print("Received ")
    print(request)
    print(" from Client")
    # hier Logik einbauen
    # An die Webseite schicken
    # Muss der Client noch mehr Infos verschicken? Eventuell nen Header in  der Nachricht? Maybe verschiedene Routen?
    # Wie starte ich die anderen Python Scripte? EInfach importieren? oder mit Subprocess?

    
    


    client_socket.close()
    print("Connection closed")

if __name__ == '__main__':
    start_server()

#gorila and gin frameworks for go
#marshall and unmarshall for json files
#