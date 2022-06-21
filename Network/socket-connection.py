import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

data_received = ''
f_handle = open('romeo.txt', 'w')

while True :
    data = mysock.recv(1000)
    if len(data) < 1 :
        break
    data_received = data.decode()

mysock.close()

split_data = data_received.split('\r\n\r\n')
f_handle.write(split_data[1].strip())