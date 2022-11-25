# Editer : ding kai
# Function : ...
# Date : 2022/11/12 00:13
from pprint import pprint

from tools.xmloperation import xml2Dict, prettyXml, dict2Yaml
import xmltodict

json_str = '''{"service": {"APP_HEAD": {"BrchCd": "043400", "LglCd": "043", "TlrNo": "ABS00001"}, "SYS_HEAD": {"ChnlTp": "313", "CnsmrCd": "300407", "CnsmrSeqNo": "300000102310231231230"}, "BODY": {"OprLng": "CHINESE","AtLndrngInfoModStruct": "3"}}} '''

if __name__ == '__main__':
    with open('abs-request.xml') as f:
        dct = xmltodict.parse(f.read())

