# Editer : ding kai
# Function : 生成xml报文
# Date : 2022/11/11 18:42
# -*- coding:utf-8 -*-

from xml.dom.minidom import Document

doc = Document()
# 根节点
root = doc.createElement("service")
doc.appendChild(root)
list_service = ['APP_HEAD', 'SYS_HEAD', 'BODY']
APP_HEAD = {'BrchCd': '043400', 'LglCd': '043', 'TlrNo': 'ABS00001'}
SYS_HEAD = {'ChnlTp':'313', 'CnsmrCd':'300407', 'CnsmrSeqNo':'300000102310231231230'}
# BODY = {'OprLng':'CHINESE', 'AtLndrngInfoModStruct': {'TranCntprCstChrctrstc':'2'}}
BODY = {'OprLng':'CHINESE', 'AtLndrngInfoModStruct': '3'}

# 二级节点 APP_HEAD
for node in list_service:
    second_node = doc.createElement(node)
    root.appendChild(second_node)
    if node == 'APP_HEAD':
        for k, v in APP_HEAD.items():
            child = doc.createElement(k)
            second_node.appendChild(child)
            child_value = doc.createTextNode(v)
            child.appendChild(child_value)
    elif node == 'SYS_HEAD':
        for k, v in SYS_HEAD.items():
            child = doc.createElement(k)
            second_node.appendChild(child)
            child_value = doc.createTextNode(v)
            child.appendChild(child_value)
    elif node == 'BODY':
        for k, v in BODY.items():
            child = doc.createElement(k)
            second_node.appendChild(child)
            child_value = doc.createTextNode(v)
            child.appendChild(child_value)
# 填充二级节点内叶子节点



# # 二级节点 APP_HEAD
# child_apphead = doc.createElement("APP_HEAD")
# root.appendChild(child_apphead)
#
# child1 = doc.createElement('BrchCd')
# child_apphead.appendChild(child1)
# brchCd_value = doc.createTextNode("043400")
# child1.appendChild(brchCd_value)

xmlFileName = "normalCredit_01.xml"

file = open(xmlFileName, "w")
file.write(doc.toprettyxml(indent='\t'))
# doc.writexml(file, indent='\t', newl='\n', addindent='\t', encoding='UTF-8')
file.close()