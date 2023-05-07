from Server import Server
from modules.Auth import Auth
# TODO:
#    Обработка ввода команд и общения сервер<->клиент

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
