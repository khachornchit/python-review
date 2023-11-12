# networking/tcp_client.py
import socket


def tcp_client():
    host = '127.0.0.1'
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input("->")
    while message.lower() != 'q':
        client_socket.send(message.encode('utf-8'))
        data = client_socket.recv(1024).decode('utf-8')
        print("Received from server:", data)
        message = input("-> ")
    client_socket.close()


if __name__ == "__main__":
    tcp_client()
