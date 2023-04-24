import socket

class Client:
    def __init__(self, conn='', addr=''):
        self.conn = socket.socket()
        self.addr = addr
    def connect(self, host='localhost', port=9090):
        self.conn.connect((host, port))
    def recv(self, bytes = 1024):
        self.data = data = self.conn.recv(bytes).decode()
        print('Получили: '+self.data)

        return data

    def send(self, d=''):
        data = d
        if d == '':
            data = self.data
        self.conn.send(data.encode('UTF-8'))
        print('Отправили: '+data)

    def disConnect(self):
        self.send('exit')
        print('Клиент отключился')


sock = Client()

host = input('Введите хост(def: localhost): ')
host = host if host != '' else 'localhost'
port = input('Введите порт(def: 9090): ')
port = port if port != '' else 9090

sock.connect(host, port)

sock.send('hello, world!')

data = sock.recv(1024)
sock.disConnect()

print(data)