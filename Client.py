import Connected, socket, os, json
class Client(Connected.Connected):
    def __init__(self, conn='', addr=''):
        self.conn = socket.socket()
        self.addr = addr
        self.prefix = 'logs'
        self.log_file_name = 'client.log'
        self.log_file = self.prefix + '/' + self.log_file_name

    def connect(self, host='localhost', port=9090):
        self.conn.connect((host, port))

    def disConnect(self):
        # self.send('exit')
        self.add_log('Вы отключились от сервера')
