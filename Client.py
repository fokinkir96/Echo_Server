import Connected, socket
from modules.Logging import Logging
class Client(Connected.Connected):
    def __init__(self):
        self.conn = socket.socket()
        self.log = Logging('client')
        self.msgs = []

    def connect(self, host='localhost', port=9090):
        result = self.conn.connect_ex((host, port))
        if result == 0:
            self.log.add_log('Вы подключились к серверу '+str(host)+':'+str(port))
        else:
            self.log.add_log('Ошибка при подключении к серверу ' + str(host) + ':' + str(port))
            self.log.add_log('Код ошибки: ' + str(result))

    def save_cookie(self, data):
        with open('sessions.txt', 'a+') as f:
            f.write(data['sess_id']+' '+data['expires']+'\n')

    def disConnect(self):
        self.send('exit')
        self.log.add_log('Вы отключились от сервера')
