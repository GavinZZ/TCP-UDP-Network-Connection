import sys
from socket import *

def checkInputNum():
    if (len(sys.argv) != 5):
        # this checks for the number of arguments
        print('Incorrect number of arguments')
        exit()

def checkPortNumber(serverPort):
    if (int(serverPort) not in range(1024, 65536)):
        # check if the input port number is in range
        print('Server Port is out of range')
        exit()

def main():
    checkInputNum()
    serverAddress = sys.argv[1]
    serverPort = sys.argv[2]
    checkPortNumber(serverPort)
    requestCode = sys.argv[3]
    message = sys.argv[4]

    # create client socket
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverAddress, int(serverPort)))
    clientSocket.send(requestCode.encode())

    # receive the rPort value from server
    rPort = clientSocket.recv(1024).decode()
    clientSocket.close()

    if (rPort != ''):
        # create UDP Client Socket
        udpSocket = socket(AF_INET, SOCK_DGRAM)
        udpSocket.sendto(message.encode(), (serverAddress, int(rPort)))
        modifiedMessage, serverAddress = udpSocket.recvfrom(2048)

        print(modifiedMessage.decode())
    else:
        print('Invalid Request Code')
        exit()

main()