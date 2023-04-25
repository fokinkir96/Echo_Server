import socket

# TODO:
#   1. save token after login
class Client:
    def __init__(self, conn='', addr=''):
        self.conn = socket.socket()
        self.addr = addr
    def connect(self, host='localhost', port=9090):
        self.conn.connect((host, port))
    def recv(self, bytes = 1024):
        self.data = data = self.conn.recv(bytes).decode()
        # print('Получили: '+self.data)
        print(data)

        return data

    def send(self, d=''):
        data = d
        if d == '':
            data = self.data
        self.conn.send(data.encode('UTF-8'))
        # print('Отправили: '+data)

    def disConnect(self):
        self.send('exit')
        print('Вы отключились')


sock = Client()

host = input('Введите хост(def: localhost): ')
host = host if host != '' else 'localhost'
port = input('Введите порт(def: 9090): ')
port = int(port) if port != '' else 9090

sock.connect(host, port)

while True:
    data = sock.recv(1024)

    cmd = input('>:')
    if cmd == 'exit':
        sock.disConnect()
        break
    sock.send(cmd)
