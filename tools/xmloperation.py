# Editer : ding kai
# Function : json、xml、dict互相转换
# Date : 2022/11/11 22:56
import logging
import os

import xmltodict
import json
import dicttoxml
import lxml.etree as etree
from xml.dom.minidom import parseString
from tools.pathoperation import getAssignPath
from tools.serialnogenerator import getSerialNoList
import datetime
import yaml
from tools.logger import logger

log = logger()
def xml2Dict(fullpath: str) ->dict:
    """
    :param fullpath:
    :return: dict
    """
    with open(fullpath, 'r', encoding='utf-8') as f:
        xmlStr = f.read()
    str_dict = xmltodict.parse(xmlStr)
    return str_dict

def xml2CaseYml(src_file: str, target_file_path: str) :
    xml_suffix = ".xml"
    yml_suffix = ".yml"
    xml_list = [file for file in os.listdir(src_file) if file.endswith(xml_suffix)]
    case_list_yml = []
    prefix = ""
    for file in xml_list:
        prefix = file[:file.find("_")]
        request_xml_dict = xml2Dict(src_file+'/'+file)
        case_dict = {"request" : request_xml_dict}
        case_dict.update({"describe" : "'## 请删除此文字，并添加案例描述..."}) # 设置案例描述
        case_dict.update({"expectedResponse" : "## 请删除此文字，并对应层级关系添加用例返回预期【key：value】..."}) # 设置用例返回值
        case_list_yml.append(case_dict)

    with open(target_file_path + '/' + prefix + yml_suffix, 'w', encoding='utf-8') as f:
        yaml.dump(case_list_yml, f, allow_unicode=True)

def xml2Json(fullpath: str):
    return json.dumps(xml2Dict(fullpath))


#  此方法返回的xml未美化
def json2Xml(jsonStr, xmlPath: str):
    dct = json.loads(jsonStr)
    bys = dicttoxml.dicttoxml(dct, root=False, attr_type=False).decode('utf-8')
    with open(xmlPath, 'w', encoding='utf-8') as xmlFile:
        xmlFile.write(bys)
    return xmlPath


# 美化xml文件
def prettyXml(xmlFile):
    root = etree.parse(xmlFile)
    print(etree.tostring(root, pretty_print=True, encoding='unicode'))
    # 覆盖自己
    root.write(xmlFile, encoding='utf-8', pretty_print=True, xml_declaration=True)


def dict2Yaml(dct):
    return yaml.dump(dct)


# 计算xml报文长度
def calXmlLength(xmlFile):
    root = etree.parse(xmlFile)
    bys = etree.tostring(root, encoding='utf-8')
    print(bys.decode('UTF-8'))
    return len(bys)


def replaceNodeValue(xmlDict: dict, ymlDict: dict, subSysNo: str) -> dict:
    """
    :param xmlDict: 源xml字典
    :param ymlDict: 配置文件中要替换的字典
    :param subSysNo: 子系统编号
    :return: 替换对应节点后的字典
    """
    # try:
    #     if ymlDict['service']['SYS_HEAD']['CnsmrCd']:  # KeyError
    #         subSysNo = ymlDict['service']['SYS_HEAD']['CnsmrCd']
    #         assert len(subSysNo) == 6  # AssertionError
    #     elif xmlDict['service']['SYS_HEAD']['CnsmrCd']:
    #         subSysNo = xmlDict['service']['SYS_HEAD']['CnsmrCd']
    #         assert len(subSysNo) == 6
    #     else:
    #         log.error('请求报文中子系统编号不正确！')
    # except KeyError as ke:
    #     log.error('报文标签配置错误,可能缺少CnsmrCd?', exc_info=True)
    #     raise ke
    # except AssertionError as ae:
    #     log.error('系统编号配置错误，不是6位', exc_info=True)
    #     raise ae
    # except Exception as e:
    #     log.error('内部错误', exc_info=True)
    #     raise e
    node_list = ['serialNo', 'date', 'time']
    for yml_k, yml_v in ymlDict.items():
        for xml_k, xml_v in xmlDict.items():
            if yml_k == xml_k:
                # 该标签需指定值替换，直接使用配置文件中的值替换报文对应的标签值
                if type(xml_v) == str :
                    if type(yml_v) not in node_list:
                        xmlDict[xml_k] = yml_v
                    # 该标签需自动生成对应类型的值替换
                    else :
                        if yml_v == 'seriaNo':
                            # 按ESB规则自动生成流水号, 规则：6位子系统编码 + 8位系统交易日期 + 18位序列号
                            date = datetime.datetime.now().strftime('%Y%m%d')
                            serialNo = getSerialNoList(1)[0]
                            xmlDict[xml_v] = subSysNo+date+serialNo
                            break
                        elif yml_v == 'date':
                            xmlDict[xml_v] = datetime.datetime.now().strftime("%Y%m%d")
                            break
                        elif yml_v == 'time':
                            xmlDict[xml_v] = datetime.datetime.now().strftime("%H%M%S")
                            break
                        else:
                            raise Exception(f'{xml_v}类型未定义')
                # 该标签的值是字典,递归查找
                elif type(xml_v) == dict:
                    replaceNodeValue(xml_v, yml_v)
                elif xml_v is None:
                    raise  Exception('请填写正确的要替换的字段类型->{}'.format(node_list))
                else:
                    raise Exception("未知的标签值类型")

    return xmlDict

def dict2prettyxml(xmlDict: dict) -> str:
    xml_bytes = dicttoxml.dicttoxml(xmlDict, root=False, attr_type=False)
    prettyxml = parseString(xml_bytes).toprettyxml(indent='\t')
    return prettyxml

if __name__ == '__main__':
    # print(readXml('normalCredit_01.xml'))
    # dct = ConvertXmlJsonDict().xml2Dict('normalCredit_01.xml')
    # print(dct)
    # print(xml2Json('normalCredit_01.xml'))
    # json_str = '''{"service": {"APP_HEAD": {"BrchCd": "043400", "LglCd": "043", "TlrNo": "ABS00001"}, "SYS_HEAD": {
    # "ChnlTp": "313", "CnsmrCd": "300407", "CnsmrSeqNo": "300000102310231231230"}, "BODY": {"OprLng": "CHINESE",
    # "AtLndrngInfoModStruct": "3"}}} '''
    # json2Xml(json_str, 'request111.xml')

    # prettyXml('request111.xml')
    # calXmlLength('abs-normalCredit_01.xml')
    # replaceXmlNodeValue(getYamlData.get_yaml_data('../data/nomalCredit-update.yml'))
    # ret = replaceNodeValue(get_yaml_data_dict(getAssignPath('auto-test', 'configs/case/testX.yml')), get_yaml_data_dict(getAssignPath('auto-test', 'configs/case/testY.yml')))
    # print(ret)
    # print(type(ret), '\n', ret)
    # calXmlLength('request01.xml')
    xml2CaseYml(getAssignPath("auto-test", "transfer"), getAssignPath("auto-test", "data/case_data"))
