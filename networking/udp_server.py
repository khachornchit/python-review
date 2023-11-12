import socket


def udp_server():
    """UDP server implementation."""
    host = '127.0.0.1'
    port = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print("Server started ...")
    while True:
        data, addr = server_socket.recvfrom(1024)
        data = data.decode('utf-8')
        print("Message from:", str(addr))
        print("From connected user:", data)
        data = data.upper()
        print("Sending:", data)
        server_socket.sendto(data.encode('utf-8'), addr)
        if data == 'Q':
            break
    server_socket.close()


if __name__ == '__main__':
    udp_server()
