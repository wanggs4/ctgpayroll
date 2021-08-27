# coding:utf-8
import requests,json,datetime,time
import unittest

class MyTestSuite(unittest.TestCase):

    def setUp(self):
        self.urlhost = 'https://autodiscover.ctgpayroll.com'
        '''域名'''
        self.urllogin_app = 'https://autodiscover.ctgpayroll.com/ehr_saas/newMobile/login/login.mobile'
        '''app登录接口'''
        self.urlcheck='https://autodiscover.ctgpayroll.com/ehr_saas/web/attEmpLog/saveAttEmpLog.mobile'
        ''''APP打卡接口'''
        self.headers_Ntoken = {'Content-Type': 'application/json'}
        '''headers不带token'''
        self.headers_token = {'Content-Type': 'application/json','token':self.login_token()}
        '''headers带token'''
        self.urlEmpCheck_bq = 'https://autodiscover.ctgpayroll.com/ehr_saas/web/attCheckApply/saveAttCheckApply.mobile'
        '''APP补签接口'''


    '''用户成功登陆后获取token'''
    def login_token(self):
        json_param = {
                'custId': '15921595797504',
                'deviceId': '8B39DD16-3442-43DE-959D-0EE9CD0C1EE6',
                'mobile': '18612533709',
                'verificationCode': '4321' }
        r = requests.post(self.urllogin_app,data=json.dumps(json_param),headers=self.headers_Ntoken)
        return r.json()['result']['data']['token']

    def test_empCheck1(self):
        json_param = {
            'checkType': 1,
            'deviceId': 'E7F91090-FD98-49D0-9382-D37B1059D013_1',
            'latitude': '39.908654',
            'longitude': '116.518779',
            'type': 1,
            'wifiMac': '',
            'wifiName': ''
        }
        requests1 = requests.post(self.urlcheck, data=json.dumps(json_param), headers=self.headers_token)
        if requests1.json()['msg'] ==  '打卡成功':
                print('testcase1:员工打卡',requests1.json()['msg'])
        elif requests1.json()['msg'] !='打卡成功':
                raise Exception('testcase1:test员工打卡',requests1.json()['msg'])

    def test_empOut2(self):
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
                  'picUrl': '22978355286016/27631730053120/f419bb8c3ba44f7bbd38c14b0320edf2.jpg'
        }
        requests1 = requests.post(self.urlcheck, data=json.dumps(json_param), headers=self.headers_token)
        print('testcase2:员工外勤打卡', requests1.json()['msg'])

    def test_empCheck_bq3(self):
        now_time = datetime.datetime.now()
        json_pqram={
            'checkTime': now_time.strftime ('%Y-%m-%d %H:%M:%S'),
            'checkType':1,
            'remark':'测试补签上班',
            'saveType':1,
        }
        requests1 = requests.post(self.urlEmpCheck_bq,data=json.dumps(json_pqram),headers=self.headers_token)
        print('testcase3:测试补签上班',requests1.text)

class SequentialTestLoader(unittest.TestLoader):
    def getTestCaseNames(self, testCaseClass):
        test_names = super().getTestCaseNames(testCaseClass)
        testcase_methods = list(testCaseClass.__dict__.keys())
        test_names.sort(key=testcase_methods.index)
        return test_names

if __name__ == '__main__':
    unittest.main (testLoader=SequentialTestLoader( ))