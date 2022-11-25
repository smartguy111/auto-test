# Editer : ding kai
# Function : tcp协议发送socket
# Date : 2022/11/11 15:05


# -*- coding: utf-8 -*-
import socket
from tools.logger import logger
from decorator.timeoutDecorator import time_out, func_set_timeout

# 使用tcp发送请求报文
@time_out
@func_set_timeout(5)
def sendMsgByTcp(ip, port, msg: str) ->bytes:
    '''
    :param ip: server ip
    :param port: server port
    :param msg:  msg
    :return: 返回响应信息：bytes
    '''
    log = logger()
    bys = msg.encode('utf-8')  # 转为字节数组
    address = (ip, port)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(address)
    client.send(bys)
    log.info('报文发送成功')
    #  todo 大于1024？
    data = client.recv(4096)  # 接受响应信息

    log.info('接收响应报文' + data.decode('utf-8'))

    client.close()

    return data

# 使用tcp发送请求报文
@time_out
@func_set_timeout(5)
def sendMsgByHttp(ip, port, msg: str):

    # TODO http方式请求
    pass


