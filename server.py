import sys
import random
from socket import *

def string_reverse(string):
    # function for reverse the string
    return string[::-1]

def main():
    requestCode = sys.argv[1]
    serverPort = 12023
    serverSocket = socket(AF_INET, SOCK_STREAM)
    while True:
        # if a port is in use, add one to serverPort
        # until find a port that's not in used
        try:
            serverSocket.bind(('', serverPort))
            break
        except:
            serverPort += 1
    print('SERVER_PORT=' + str(serverPort))

    serverSocket.listen(1)

    while True:
        connectionSocket, addr = serverSocket.accept()
        rCode = connectionSocket.recv(1024)
        if (rCode.decode() != requestCode):
            # if request code doesn't match, exit the program
            connectionSocket.close()
            print('Server closed due to incorrect request code')
            exit()
        else:
            udpServerSocket = socket(AF_INET, SOCK_DGRAM)
            # udpServerSocket.bind(('', int(rPort)))
            
            rPort = random.randrange(1024, 65536)
            while True:
                # if a port is in use, add one to serverPort
                # until find a port that's not in used
                try:
                    udpServerSocket.bind(('', rPort))
                    break
                except:
                    serverPort += 1

            connectionSocket.send(str(rPort).encode())
            connectionSocket.close()

            # create UDP Server Socket

            message, clientAddress = udpServerSocket.recvfrom(2048)
            modifiedMessage = string_reverse(message.decode())
            udpServerSocket.sendto(modifiedMessage.encode(), clientAddress)
            udpServerSocket.close()

main()

