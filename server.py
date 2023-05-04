import socket, Logging, Connected

# TODO:
#    Обработка ввода команд и общения сервер<->клиент


# class Auth:
#     def __init__(self, sock):
#         self.sock = sock
#
#     def get_login_data(self):
#         name = self.get_client_name()
#         self.greet_client()
#         if self.pwd == False:
#             self.set_password()
#             # Если нет пароля, то:
#             #   1. Просим пароль
#             #   2. Сохраняем хеш пароля
#             #   3. Отправляем токен со временем и сохраняем в файл ip:токен
#             #   4. Profit
#             pass
#         else:
#             pwd = self.get_client_password()
#             # Если есть токен, то:
#             #   1. чекаем валидность токена
#
#             # Если есть пароль, то:
#             #   1. Просим пароль
#             #   2. Проверяем хеши
#             #   3. Если ок, то profit(send token to client)
#             #   4. Если не ок, то просим еще раз(3 попытки)
#             #   5. Profit
#             pass

class Server(Logging.Logging):

    def __init__(self, host = 'localhost', port = 9090, quantity = 5):
        super().__init__()
        self.host = host
        self.port = port
        self.quantity = quantity
        self.connected = []
        self.sock = self.start()

    def start(self):
        sock = socket.socket()

        try:
            sock.bind((self.host, self.port))
        except Exception:
            while True:
                try:
                    self.port += 1
                    sock.bind((self.host, self.port))
                    break
                except Exception:
                    pass

        self.add_log('Сервер запущен')

        sock.listen(self.quantity)
        self.add_log('Слушаем ' + str(self.host) + ' на ' + str(self.port) + ' порту')

        return sock

    def wait_client(self):
        c, addr = self.sock.accept()
        cl = Connected.Connected(c, addr)
        self.connected.append(cl)

        self.add_log('Клиент '+str(cl.addr[0])+':'+str(cl.addr[1])+' подключился')
        return cl
    def stop(self):
        self.add_log('Сервер остановлен')
        exit()


s = Server()

while True:
    client = s.wait_client()
    data = False
    while data != 'exit':
        data = client.recv(1024)
        if data == '':
            break
        client.send(data)
    else:
        client.disConnect()
