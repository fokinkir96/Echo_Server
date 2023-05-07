import Client

# TODO:
#   1. save token after login

sock = Client.Client()

host = input('Введите хост(def: localhost): ')
host = host if host != '' else 'localhost'
port = input('Введите порт(def: 9090): ')
port = int(port) if port != '' else 9090

sock.connect(host, port)

while True:
    data, type = sock.recv(1024)

    if type == 'info':
        print(data)
        cmd = input('>:')
    elif type == 'prompt':
        cmd = input(data+'>:')
    elif type == 'cookie':
        sock.save_cookie(data)
    if cmd == 'exit':
        sock.disConnect()
        break
    sock.send(cmd)
