# Editer : ding kai
# Function : 普通贷记接口测试案例
# Date : 2022/11/11 18:31

import allure
import pytest
import os
from lib.apiLib.upp.payment import Payment
from tools.cleanstuff import cleanTestFile
from tools.getyamldata import get_yaml_data_list
from tools.logger import logger
from tools.xmloperation import dict2prettyxml
from tools.pathoperation import getAssignPath, getRootPath

rootPath = getRootPath('auto-test')
reportPath = getAssignPath('auto-test', 'report/tmp/')
yamlPath = getAssignPath('auto-test', 'data/case_data/')



# 测试类 - 标签mark
@allure.epic("统一支付系统-史诗级别测试epic")
@allure.feature("支付模块")
@pytest.mark.payment_all
class TestPayment:
    # 每个类下面所有的方法调用，此方法只运行一次
    def setup_class(self):
        pass

    # 定义测试方法 - 普通贷记
    # 按需使用fixture
    @allure.story('普通贷记')
    @allure.title('普通贷记测试用例')
    @allure.issue('https://www.baidu.com', name='链接（集成其他测试管理工具使用）')
    # @allure.testcase('https://www.baidu.com', name='链接（集成其他测试管理工具使用）')
    @allure.severity('blocker') #blocker阻塞的， normal正常的（默认）， minor轻微的
    # 对测试方法mark
    @pytest.mark.normal_credit
    @pytest.mark.usefixtures('normal_credit_init') # 使用fixture，有返回值时不能使用
    # get_yaml_data_list返回值会传入reqData, respData
    @pytest.mark.parametrize('reqData, respData',
                             get_yaml_data_list(
                                 yamlPath + '/payment.yml'))
    def test_normal_credit(self, reqData: dict, respData: dict):
        """
        1- 根据请求报文发送ESB普通贷记接口
        2- 比对ESB返回的响应报文的msg 与 用例中预期msg是否一致
        """
        log = logger()
        print(type(reqData))
        # 1 将reqData转换为xml字符流
        payload = reqData
        reqXml = dict2prettyxml(payload)
        log.info('test_normal_credit 请求报文： \n' + reqXml)
        # 2 生成xml文件
        currentPath = os.getcwd().replace('\\', '/').strip()  # 获取当前路径
        # xmlFile = '' + currentPath + '/normal_credit.xml'
        xmlFile = '%s%s' % (currentPath, '/normal_credit.xml')
        with open(xmlFile, 'w', encoding='utf-8') as f:
            f.write(reqXml)
        # 3 发送接口, 得到响应报文
        resp = {}
        try:
            resp = Payment().normal_credit(xmlFile)
            log.info("test_normal_credit 响应报文: \n " + dict2prettyxml(resp))
        except Exception as e :
            log.info("调用esb接口异常,请检查")
            raise e

        # 4 断言
        try:
            assert resp['service']['BODY']['msg'] == respData['msg']
        except Exception as e :
            log.exception("断言失败！！")
            raise e





if __name__ == '__main__':

    cleanTestFile(reportPath)

    pytest.main(['test_payment.py', '--alluredir', reportPath])
    os.system('allure serve ' + reportPath)

    # 静态报告
    # allure generate.. / report / tmp - o.. / report / html - -clean
