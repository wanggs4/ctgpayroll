# coding:utf-8
import requests,json
import unittest


class MyTestSuite(unittest.TestCase):
    def setUp(self):
        self.url='https://testapi.ctgpayroll.com/ehr_saas/web/attEmpLog/saveAttEmpLog.mobile'
        self.headers = {'Content-Type': 'application/json',
               'token': 'vwTLTwYvBqCoKH+42+nOsY4yLktvj+CZ/L50SWKwPi46zyWMt0Vx3LMfOYY/Tzl6FBW1kZ6AeTQmqfEueTwebQ=='}

    def test_start(self):
        json_param = {
                  'checkType': 1,
                  'deviceId': 'E7F91090-FD98-49D0-9382-D37B1059D013_1',
                  'latitude': '39.908654',
                  'longitude': '116.518779',
                  'type': 1,
                  'wifiMac': '',
                  'wifiName': ''}
        requests1 = requests.post(self.url, data=json.dumps(json_param), headers=self.headers)
        print('testcase:test_start',requests1.text)

    def test_end(self):
        json_param = {
                  'checkType':2,
                  'deviceId': 'E7F91090-FD98-49D0-9382-D37B1059D013_1',
                  'latitude': '39.908654',
                  'longitude': '116.518779',
                  'type': 1,
                  'wifiMac': '',
                  'wifiName': ''}
        requests1 = requests.post(self.url, data=json.dumps(json_param), headers=self.headers)
        print('testcase:test_end',requests1.text)

    def test_Outside(self):
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
        print('testcase:test_Outside',requests1.text)

if __name__ == '__main__':
    unittest.main()