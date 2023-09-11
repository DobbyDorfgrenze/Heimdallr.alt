package main

import (
	"fmt"
	"net"
)

const e = "Error:"

func main() {
	// Listen for incoming connections
	listener, err := net.Listen("tcp", ":8080")
	if err != nil {
		fmt.Println(e, err)
		return
	}
	defer listener.Close()

	fmt.Println("Server started. Listening for incoming connections...")

	for {
		// Accept a client connection
		conn, err := listener.Accept()
		if err != nil {
			fmt.Println(e, err)
			continue
		}

		// Handle client request in a separate goroutine
		go handleClientRequest(conn)
	}
}

func handleClientRequest(conn net.Conn) {
	defer conn.Close()

	// Read client request
	buffer := make([]byte, 1024)
	n, err := conn.Read(buffer)
	if err != nil {
		fmt.Println(e, err)
		return
	}

	request := string(buffer[:n])
	fmt.Println("Received data:", request)

	// Send response back to the client
	response := "Server received the data successfully"
	_, err = conn.Write([]byte(response))
	if err != nil {
		fmt.Println(e, err)
		return
	}
}
