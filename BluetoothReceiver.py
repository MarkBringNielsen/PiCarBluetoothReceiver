import socket


hostMACAddress = input()
port = 3
backlog = 1
size = 1024
sckt = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket. BTPROTO_RFCOMM)
sckt.bind((hostMACAddress, port))
sckt.listen(backlog)

try:
    client, address = sckt.accept()

    while 1:
        data = client.recv(size)
        if data:
            print(data)
            client.send(data)
except:
    print("Closing socket")
    client.close()
    sckt.close()