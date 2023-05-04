import json, Logging

class Message:

    def __init__(self):
        self.conn = conn

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
