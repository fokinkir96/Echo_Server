import socket, os, datetime

# sock = socket.socket()
#
# sock.bind(('localhost', 9090))
#
# sock.listen()
#
# print(sock.getsockname()[0])
# print(sock.getsockname()[1])
#
# while True:
#     conn, addr = sock.accept()
#     print('conn:', conn)
#     print('addr:', addr)
#     print('sock:', sock)
#     data = conn.recv(1024)
#     print('data:', data)
#     # if not data:
#     #     break
#     conn.send(data.upper())

# conn.close()
# TODO:
#    Модифицируйте код сервера таким образом, чтобы он автоматически изменял номер порта, если он уже занят. Сервер должен выводить в консоль номер порта, который он слушает.
#    Обработка ввода команд и общения сервер<->клиент

class Serv:

    def __init__(self):
        self.log_file = 'logs/server.log'

    def create_log_file(self):
        if 'logs' not in os.listdir():
            os.mkdir('logs')
        log = open(self.log_file, 'a', encoding='UTF-8')
        print(log)

        return log

    def add_log(self, log):
        print(log)
        with open(self.log_file, 'a', encoding='UTF-8') as f:
            f.write(str(datetime.datetime.now())+': '+log+'\n')

class Client(Serv):
    def __init__(self, conn='', addr=''):
        super().__init__()
        self.conn = conn if conn != '' else socket.socket()
        self.addr = addr
        name = self.get_client_name(self.addr[0])
        if name == False:
            self.send('Введите свое имя: ')
            #
    def connect(self, host='localhost', port=9090):
        self.conn.connect((host, port))
    def recv(self, bytes = 1024):
        self.data = data = self.conn.recv(bytes).decode()
        self.add_log('Получили: '+self.data)

        return data

    def send(self, d=''):
        data = d
        if d == '':
            data = self.data
        self.conn.send(data.encode('UTF-8'))
        self.add_log('Отправили: '+data)

    def get_client_name(self, ip):
        with open('serv/clients.txt', 'r') as f:
            for i in f.readlines():
                i = i.split()
                if ip == i[0]:
                    return i[1]

        return False
    def disConnect(self):
        # self.send('exit')
        self.add_log('Клиент '+str(self.addr[0])+':'+str(self.addr[1])+' отключился')


class Server(Serv):

    def __init__(self, host = 'localhost', port = 80, quantity = 5):
        super().__init__()
        self.sock = self.start()
        self.host = host
        self.port = port
        self.quantity = quantity
        self.connected = []

    def start(self):
        sock = socket.socket()

        self.add_log('Сервер запущен')

        return sock

    def listen_port(self):
        self.sock.bind((self.host, self.port))
        self.sock.listen(self.quantity)
        self.add_log('Слушаем '+str(self.host)+' на '+str(self.port)+' порту')
        # print(self.sock)

    def wait_client(self):
        c, addr = self.sock.accept()
        cl = Client(c, addr)
        self.connected.append(cl)

        self.add_log('Клиент '+str(cl.addr[0])+':'+str(cl.addr[1])+' подключился')
        return cl
    def stop(self):
        self.add_log('Сервер остановлен')
        exit()


s = Server()
s.listen_port()
while True:
    client = s.wait_client()
    data = ''
    while data != 'exit':
        data = client.recv(1024)
        client.send(data)
    else:
        client.disConnect()
