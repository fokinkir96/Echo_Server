import os, datetime
class Service(Logging, Message):

    def __init__(self):
        self.log_file = 'logs/server.log'
# Logging
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

#