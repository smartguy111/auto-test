# Editer : ding kai
# Function : ...
# Date : 2022/11/13 16:55
import dicttoxml

def ceshi(reqData: dict):
    print(reqData)
    payload = reqData
    ret = dicttoxml.dicttoxml(payload)
    print((type(ret), ret.decode('UTF-8')))


if __name__ == '__main__':
    dct = {'a': 1, 'b':{'A': '中文'}}

    ceshi(dct)