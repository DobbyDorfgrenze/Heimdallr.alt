package main

import (
	"fmt"
	"net"
)

func test() {
	// Connect to the server
	conn, err := net.Dial("tcp", "localhost:8080")
	const e = "Error:"
	if err != nil {
		fmt.Println(e, err)
		return
	}
	defer conn.Close()

	// Send data to the server
	data := "Hello, Server!"
	_, err = conn.Write([]byte(data))
	if err != nil {
		fmt.Println(e, err)
		return
	}

	// Read response from the server
	buffer := make([]byte, 1024)
	n, err := conn.Read(buffer)
	if err != nil {
		fmt.Println(e, err)
		return
	}

	response := string(buffer[:n])
	fmt.Println("Server response:", response)
}
