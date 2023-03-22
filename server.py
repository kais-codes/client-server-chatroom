from socket import *

# set up server socket and then set it to reuse option to avoid being stuck on same port
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# binds the server socket, variables for readability
localhost = "127.0.0.1"
port = 2048
server_socket.bind((localhost, port))

server_socket.listen(1)

# accepts the connection with the client
client_socket, address = server_socket.accept()
print("You have connected to the client")
print("Enter /q to end connection")
print("Waiting for incoming message...")

while True:
    # receives message from client, checks if /q from incoming
    incoming = client_socket.recv(4096).decode()

    if not incoming:
        print("Connection closed by client.")
        server_socket.close()
        break
    else:
        print("Client: ", incoming)

    # send outgoing message
    outgoing = input()

    # /q detected is detected and quit, else a message is sent
    if outgoing == "/q":
        print("You have ended the connection with the client")
        server_socket.close()
        break
    else:
        outgoing = outgoing.encode('utf-8')
        client_socket.send(outgoing)







