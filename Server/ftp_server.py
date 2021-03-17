import socket
import pathlib
from os import listdir
from os.path import isfile, join


def server():
    while 1:
        print("Awaiting Client Connection...")
        s = socket.socket()
        HOST = '127.0.0.1'
        PORT = 20000
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        print('Connected by', addr)

        while True:
            # Receive the data and convert it back into a string
            data = conn.recv(1024).decode()
            dataString = str(data).split()

            # If we have a get request let's return the requested file
            if dataString[0] == 'Retrieve':
                file = open(dataString[1], 'rb')
                file_data = file.read(1024)
                conn.send(file_data)

            elif dataString[0] == 'List':
                mypath = pathlib.Path().absolute()
                onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
                fileList = ""
                for f in onlyfiles:
                    fileList = fileList + f + " "
                conn.sendall(fileList.encode())

            elif dataString[0] == 'Store':
                file = open(dataString[1], 'wb')
                data = ' '.join(data.split(' ')[2:])
                file_data = data.encode()
                file.write(file_data)
                file.close()

            elif dataString[0] == 'Quit':
                s.close()
                print("Client has ended the connection...")
                break

        conn.close()


if __name__ == '__main__':
    server()
