# Editer : ding kai
# Function : 付款类接口
# Date : 2022/11/11 14:51
import json
import socket

import xmltodict
from tools.sendmsg import sendMsgByTcp


class Payment:
    # 1 获取环境信息、基础配置、token等
    def __init__(self):
        pass

    # 2 30041000001(普通贷记)
    def normal_credit(self, xmlMsgPath: str) -> dict:
        """
        30041000001(普通贷记)接口
        :param xmlMsgPath: xml报文路径
        :return: str 响应报文
        """
        with open(xmlMsgPath, encoding='utf-8') as f:
            xml = f.read()
        # TODO tcp/http
        msg = sendMsgByTcp('127.0.0.1', 12333, xml)

        # 将响应转为字典格式并返回
        return xmltodict.parse(msg.decode('utf-8'))


if __name__ == '__main__':
    ret = Payment().normal_credit('/Users/dingkai/python/pythonProjects/auto-test/mock/request01.xml')
    print(type(ret), ret)
