import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))
server_socket.listen(1)
firstVersion = False

while True:
    client_socket, client_address = server_socket.accept()
    content = client_socket.recv(1024).decode("utf-8")
    if not firstVersion:
        print("Received first version:", content)
        firstVersion = True
    else:
        print("Received updated version:", content)

    client_socket.close()
