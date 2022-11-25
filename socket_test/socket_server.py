# Editer : ding kai
# Function : TCP服务端
# Date : 2022/11/11 15:27

import socket

# 1 创建socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2 绑定host port
server.bind(('127.0.0.1', 7001))
# server.bind(('0.0.0.0', 7001))

# 3 监听
server.listen()

print('等待客户端的连接')

# 4 等待接收客户端的连接
client, address = server.accept()
print(f'{address}已连接')

# 5 向客户端发送消息
client.send('hello.... 你好'.encode('utf-8'))

# 6 等待客户端发来消息
msg = client.recv(1024)  # 阻塞
print(address, '说： ', msg.decode())

client.close()
server.close()
