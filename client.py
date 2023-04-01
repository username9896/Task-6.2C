import socket

clientsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
localhost = socket.gethostname()

port = 6001

while True:
    Userinput = input("Enter the hostname or type 'quit' to exit: ")

    if Userinput.lower() == 'quit':
        break

    clientsock.sendto(Userinput.encode(), (localhost, port))
    response, addr = clientsock.recvfrom(2048)
    print("Response from the server: " + str(response.decode()))

    ask_query = input("Want to make another query (yes/no): ")

    if ask_query.lower() == 'no':
        break

clientsock.close()
