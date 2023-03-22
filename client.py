from socket import *

# info for connecting
localhost = "127.0.0.1"
port = 2048

client_socket = socket(AF_INET, SOCK_STREAM)

client_socket.connect((localhost, port))
print("You have connected to the server")
print("Enter /q to end connection")

while True:
    # outgoing message, checks for /q
    outgoing = input()

    if outgoing == "/q":
        print("You have closed the connection")
        client_socket.close()
        break

    # message is valid, sends to server
    outgoing = outgoing.encode('utf-8')
    client_socket.send(outgoing)

    # receives message from the server. checks for /q
    incoming = client_socket.recv(4096).decode()
    if not incoming:
        print("Connection closed by server")
        client_socket.close()
        break

    print("Server: ", incoming)




