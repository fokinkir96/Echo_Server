import socket

sock = socket.socket()

sock.bind(('', 9090))

sock.listen(1)

# print(addr)

while True:
    conn, addr = sock.accept()
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data.upper())

# conn.close()