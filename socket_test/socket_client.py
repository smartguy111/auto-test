# Editer : ding kai
# Function : socket客户端
# Date : 2022/11/11 15:37

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 7001))
client.send('hi'.encode('utf-8'))
msg = client.recv(1024)  # 阻塞
print('Server: ', msg.decode('utf-8'))

client.send('nihao......'.encode('utf-8'))

client.close()



