import socket, os, datetime

# TODO:
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

    def __init__(self, host = 'localhost', port = 6463, quantity = 5):
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
        cl = Client(c, addr)
        self.connected.append(cl)

        self.add_log('Клиент '+str(cl.addr[0])+':'+str(cl.addr[1])+' подключился')
        return cl
    def stop(self):
        self.add_log('Сервер остановлен')
        exit()


s = Server()

while True:
    client = s.wait_client()
    data = ''
    while data != 'exit':
        data = client.recv(1024)
        client.send(data)
    else:
        client.disConnect()
