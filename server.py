import socket

sock = socket.socket()

sock.bind(('localhost', 9090))

sock.listen()

print(sock.getsockname()[0])
print(sock.getsockname()[1])

while True:
    conn, addr = sock.accept()
    print('conn:', conn)
    print('addr:', addr)
    print('sock:', sock)
    data = conn.recv(1024)
    print('data:', data)
    # if not data:
    #     break
    conn.send(data.upper())

# conn.close()
# class Server:
#
#     def __init__(self):
#         self.sock = self.start()
#
#     def start(self, host = '', port = 9090):
#         sock = socket.socket()
#
#         sock.bind((host, port))
#
#         print('Сервер запущен')
#
#         return sock
#
#     def listen_port(self, quantity = 1):
#         sock.listen(quantity)
#         print('Слушаем порт')
#         print(self.sock)
#
#     def cl_connect(self):
#         conn, addr = sock.accept()
#         print('Клиент подключился')
#
#     def get_data(self):
#         print('Получили: ')
#
#     def send_data(self):
#         print('Отправили: ')
#
#     def cl_disConnect(self):
#         print('Клиент отключился')
#
#     def stop(self):
#         print('Сервер остановлен')
#
