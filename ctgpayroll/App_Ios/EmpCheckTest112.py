# coding:utf-8
import requests,json
import unittest
from ctgpayroll.myLogin.login import login
from ctgpayroll.Url.myurl import url


class MyTestSuite(unittest.TestCase):

    def test_empCheck1(self):
        json_param = {
            'checkType': 1,
            'deviceId': 'E7F91090-FD98-49D0-9382-D37B1059D013_1',
            'latitude': '39.908654',
            'longitude': '116.518779',
            'type': 1,
            'wifiMac': '',
            'wifiName': ''}
        self.headers = {'Content-Type': 'application/json','token':login.login_token()}
        requests1 = requests.post(url.urlcheck, data=json.dumps(json_param), headers=self.headers)
        if requests1.json()['msg'] ==  '打卡成功':
                print('case1:test员工打卡1',requests1.json()['msg'])
        elif requests1.json()['msg'] !='打卡成功':
                raise Exception('case1:test员工打卡1',requests1.json()['msg'])

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
                  'picUrl': '22978355286016/27631730053120/f419bb8c3ba44f7bbd38c14b0320edf2.jpg'}
        requests1 = requests.post(self.url, data=json.dumps(json_param), headers=self.headers)
        print('case2:test员工外勤2', requests1.json()['msg'])

class SequentialTestLoader(unittest.TestLoader):
    def getTestCaseNames(self, testCaseClass):
        test_names = super().getTestCaseNames(testCaseClass)
        testcase_methods = list(testCaseClass.__dict__.keys())
        test_names.sort(key=testcase_methods.index)
        return test_names

if __name__ == '__main__':
    unittest.main (testLoader=SequentialTestLoader( ))