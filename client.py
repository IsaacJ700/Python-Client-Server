import socket
import sys


def client():
    while 1:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        command = input("Enter Command\n")
        commandOption = command.split()
        if commandOption[0] == 'Connect':
            s.connect((commandOption[1], int(commandOption[2])))
            print("Connected to the Server!\n")
            while 1:
                command = input("Enter Command\n")
                commandOption = command.split()
                if commandOption[0] == 'Retrieve':
                    file = open(commandOption[1], 'wb')
                    s.sendall(command.encode())
                    file_data = s.recv(1024)
                    file.write(file_data)
                    file.close()
                elif commandOption[0] == 'List':
                    s.sendall(commandOption[0].encode())
                    fileList = s.recv(1024).decode().split()
                    print("Files in Server Directory: \n")
                    for f in fileList:
                        print(f + '\n')

                elif commandOption[0] == 'Store':
                    file = open(commandOption[1], 'rb')
                    file_data = file.read(1024)
                    command = command + " " + file_data.decode()
                    s.sendall(command.encode())

                elif commandOption[0] == 'Quit':
                    s.sendall(commandOption[0].encode())
                    s.close()
                    print("Connection ending...")
                    return
                else:
                    print(
                        "Try entering one of the following commands: \'List\', \'Retrieve <filename>\', \'Store "
                        "<filename>\', or \'Quit\' ")

        else:
            print('Try connecting to a sever using the \'Connect <server name/IP address> <server port>\' command')


if __name__ == '__main__':
    client()
