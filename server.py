import socket, os, datetime, json

# TODO:
#    Обработка ввода команд и общения сервер<->клиент


class Auth:
    def __init__(self, sock):
        self.sock = sock

    def get_login_data(self):
        name = self.get_client_name()
        self.greet_client()
        if self.pwd == False:
            self.set_password()
            # Если нет пароля, то:
            #   1. Просим пароль
            #   2. Сохраняем хеш пароля
            #   3. Отправляем токен со временем и сохраняем в файл ip:токен
            #   4. Profit
            pass
        else:
            pwd = self.get_client_password()
            # Если есть токен, то:
            #   1. чекаем валидность токена

            # Если есть пароль, то:
            #   1. Просим пароль
            #   2. Проверяем хеши
            #   3. Если ок, то profit(send token to client)
            #   4. Если не ок, то просим еще раз(3 попытки)
            #   5. Profit
            pass



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

        if 'serv' not in os.listdir():
            os.mkdir('serv')

        self.name = self.get_client_name(self.addr[0])
        if self.name == False:
            self.send('Введите свое имя: ')
            self.name = self.recv()
            self.put_client_name(self.name)

        self.send('Привет, ' + self.name)
            #
    def connect(self, host='localhost', port=9090):
        self.conn.connect((host, port))
    def recv(self, bytes = 1024):
        self.data = data = json.loads(self.conn.recv(bytes))
        self.add_log('Получили: '+self.data)

        return data

    def send(self, d='', type='info'):
        data = d
        if d == '':
            data = self.data
            return

        head = self.get_header(len(data), type)
        msg = self.get_message(head, data)
        self.conn.send(msg)
        self.add_log('Отправили: '+data)

    def get_message(self, head, body):
        message = {
            'Header' :  head,
            'Body' :    body,
        }

        return json.dumps(message)
    def get_header(self, length, type):
        types = [
            'info',
            'prompt',
        ]
        if type in types:
            mtype = type
        header = {
            'Content-length': length,
            'Type': mtype,
        }

        return header
    def get_client_name(self, ip):
        with open('serv/clients.txt', 'r') as f:
            for i in f.readlines():
                print(i)
                i = i.split()
                if ip == i[0]:
                    return i[1]

        return False

    def put_client_name(self, name):
        with open('serv/clients.txt', 'a+') as f:
            f.write(str(self.addr[0])+' '+self.name+'\n')

    def disConnect(self):
        # self.send('exit')
        self.add_log('Клиент '+str(self.addr[0])+':'+str(self.addr[1])+' отключился')


class Server(Serv):

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
    data = False
    while data != 'exit':
        data = client.recv(1024)
        if data == '':
            break
        client.send(data)
    else:
        client.disConnect()
