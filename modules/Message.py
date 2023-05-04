import json, datetime

class Message:

    def __init__(self, msg, parsed=True, type='info'):
        self.head = {}
        self.pureMsg = ''

        if parsed:
            self.head['Type'] = type
            self.head['Content-length'] = len(msg)
            self.body = msg
        else:
            self.parse(msg)

    def parse(self, msg):
        self.pureMsg = msg.decode()
        data = json.loads(self.pureMsg)

        self.head = data['Header']
        self.body = data['Body']

    def prepare(self):
        self.head['DateTime'] = str(datetime.datetime.now())
        message = {
            'Header': self.head,
            'Body': self.body,
        }
        self.pureMsg = json.dumps(message)

        return self.pureMsg.encode('UTF-8')

    # def recv(self, bytes = 1024):
    #     self.data = data = json.loads(self.conn.recv(bytes))
    #     self.add_log('Получили: '+self.data)
    #
    #     return data
    #
    # def send(self, d='', type='info'):
    #     data = d
    #     if d == '':
    #         data = self.data
    #         return
    #
    #     head = self.get_header(len(data), type)
    #     msg = self.get_message(head, data)
    #     self.conn.send(msg)
    #     self.add_log('Отправили: '+data)
    #
    # def get_message(self, head, body):
    #     message = {
    #         'Header' :  head,
    #         'Body' :    body,
    #     }
    #
    #     return json.dumps(message)
    # def get_header(self, length, type):
    #     types = [
    #         'info',
    #         'prompt',
    #     ]
    #     if type in types:
    #         mtype = type
    #     header = {
    #         'Content-length': length,
    #         'Type': mtype,
    #     }
    #
    #     return header
