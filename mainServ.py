from Server import Server
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


s = Server()

while True:
    client = s.wait_client()
    data = False
    while data != 'exit':
        data, type = client.recv(1024)
        # if data == '':
        #     break
        client.send(data)
    else:
        client.disConnect()
        s.connected.remove(client)
