import socket, time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)
headersize = 10

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} stablished!")

    msg = "Welcome to my server man"
    msg = f'{len(msg):<{headersize}}' + msg

    clientsocket.send(bytes(msg, "utf-8"))

    while True:
        time.sleep(3)
        msg = f"Time doesn't stop: {time.time()}"
        msg = f'{len(msg):<{headersize}}' + msg
        clientsocket.send(bytes(msg, "utf-8"))
