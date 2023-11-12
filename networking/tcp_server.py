import socket


def main():
    """
    Listens for TCP connections and processes incoming messages.
    """
    host = '127.0.0.1'
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(1)
    client_socket, addr = server_socket.accept()
    print("Connection from:", addr)
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        print("From connected user:", data)
        data = data.upper()
        print("Sending:", data)
        client_socket.send(data.encode('utf-8'))
    client_socket.close()


if __name__ == '__main__':
    main()
