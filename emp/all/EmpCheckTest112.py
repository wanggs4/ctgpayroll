# coding:utf-8
import requests,json
import unittest


class MyTestSuite(unittest.TestCase):
    def setUp(self):
        self.url='https://autodiscover.ctgpayroll.com/ehr_saas/web/attEmpLog/saveAttEmpLog.mobile'
        self.headers = {'Content-Type': 'application/json','token':MyTestSuite.login_token()}
        self.checkLocationUrl = 'https://testapi.ctgpayroll.com/ehr_saas/web/attSetLocation/saveAttSetLocation.mobileHr'

    def login_token():
        # 用户成功登陆后获取token
        loginUrl = 'https://autodiscover.ctgpayroll.com/ehr_saas/newMobile/login/login.mobile'
        headers = {'Content-Type': 'application/json'}
        json_param = {
                'custId': '15921595797504',
                'deviceId': '8B39DD16-3442-43DE-959D-0EE9CD0C1EE6',
                'mobile': '18612533709',
                'verificationCode': '4321'
            }
        r = requests.post(loginUrl,data=json.dumps(json_param),headers=headers)
        return r.json()['result']['data']['token']

    def test_员工打卡1(self):
        json_param = {
            'checkType': 1,
            'deviceId': 'E7F91090-FD98-49D0-9382-D37B1059D013_1',
            'latitude': '39.908654',
            'longitude': '116.518779',
            'type': 1,
            'wifiMac': '',
            'wifiName': ''}
        requests1 = requests.post(self.url, data=json.dumps(json_param), headers=self.headers)
        if requests1.json()['msg'] ==  '打卡成功':
                print('1testcase:test_员工打卡1',requests1.json()['msg'])
        elif requests1.json()['msg'] !='打卡成功':
                raise Exception('1testcase:test_员工打卡1',requests1.json()['msg'])

    def test_员工外勤2(self):
        json_param = {
                  'checkAdd':'北京市朝阳区高碑店镇建国路1',
                  'checkType': 3,
                  'deviceId': 'E7F91090-FD98-49D0-9382-D37B1059D013_1',
                  'latitude': '39.908654',
                  'longitude': '116.518779',
                  'type': 1,
                  'wifiMac': '',
                  'wifiName': '',
                  'remark': '测试外勤',
                  'picUrl': '22978355286016/27631730053120/f419bb8c3ba44f7bbd38c14b0320edf2.jpg'}
        requests1 = requests.post(self.url, data=json.dumps(json_param), headers=self.headers)
        print('1testcase:test_员工外勤2', requests1.json()['msg'])

class SequentialTestLoader(unittest.TestLoader):
    def getTestCaseNames(self, testCaseClass):
        test_names = super().getTestCaseNames(testCaseClass)
        testcase_methods = list(testCaseClass.__dict__.keys())
        test_names.sort(key=testcase_methods.index)
        return test_names

if __name__ == '__main__':
    unittest.main (testLoader=SequentialTestLoader ( ))