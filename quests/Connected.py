import os
from modules.Logging import Logging
from modules.Message import Message
from modules.Auth import Auth

class Connected:
    def __init__(self, conn, addr):
        self.conn = conn

        self.addr = addr
        # self.ip = self.addr[0]+':'+self.addr[1]
        self.ip = self.addr[0]
        self.name = ''

        self.log = Logging()
        self.auth = Auth()
        self.msgs = []

    def recv(self, bytes = 1024):
        msg = Message(self.conn.recv(bytes), False)
        self.msgs.insert(0, msg)
        self.log.add_log('Получили: '+msg.pureMsg)

        return msg.body, msg.head['Type']

    def send(self, m, type='info'):
        msg = Message(m, type=type)

        self.conn.send(msg.prepare())
        self.log.add_log('Отправили: '+msg.pureMsg)

    def disConnect(self):

        # self.conn.disconnect()
        self.log.add_log('Клиент '+str(self.addr[0])+':'+str(self.addr[1])+' отключился')
