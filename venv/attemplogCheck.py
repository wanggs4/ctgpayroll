# coding:utf-8
import requests,json
import unittest


class MyTestSuite(unittest.TestCase):
    def setUp(self):
        self.url='https://testapi.ctgpayroll.com/ehr_saas/web/attEmpLog/saveAttEmpLog.mobile'
        self.headers = {'Content-Type': 'application/json',
               'token': 'vwTLTwYvBqCoKH+42+nOsY4yLktvj+CZ/L50SWKwPi46zyWMt0Vx3LMfOYY/Tzl6FBW1kZ6AeTQmqfEueTwebQ=='}
        self.checkLocationUrl = 'https://testapi.ctgpayroll.com/ehr_saas/web/attSetLocation/saveAttSetLocation.mobileHr'

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
        # print(requests1.status_code,'testcase:test_start',requests1.json()['msg'])
        # w =requests1.json()['msg']
        # print(w,w.encode('utf-8'))
        if requests1.json()['msg'] ==  '打卡成功':
                print('1testcase:test_start',requests1.json()['msg'])
        elif requests1.json()['msg'] =='所在部门没有设置打卡地点':
                # print('所在部门没有设置打卡地点')
                data1 = {
                    'deptId': '22978615332864,15189763112960,21318008938496,21420240904192,26941311627264,18851478470656,22786721398784,24623214514176,24667590250496,24721784852480,24805171810304,24846817054720,24899241660416,24946033315840,24991122083840,25040962998272,25098789867520,25147968081920,25201659367424,15818668015616,18129595719680,22670185709568',
                    'actRadius': 200,
                    'locSetName': '测试易才集团',
                    'locName': '北京市朝阳区建国路56号天洋运河F1栋',
                    'longitude': '116.518779',
                    'latitude': '39.908654'}

                r = requests.post(self.checkLocationUrl, data=json.dumps(data1), headers=self.headers)
                # time.sleep(3)
                # q = r.json()['msg']
                # print(q, q.encode('utf-8'))
                print('2testcase:test_start',r.status_code, 'testcase:test_start', r.json()['msg'])
                r.json()['msg'] == '考勤地点设置成功'
                # print(3,r.json()['msg'])
                requests2 = requests.post(self.url, data=json.dumps(json_param), headers=self.headers)
                # print(requests2.status_code, 'testcase:test_start', requests2.json()['msg'])
                print('3testcase:test_start',requests2.json()['msg'],requests2.json()['msg'].encode('utf-8'))
        else:
                print('4testcase:test_start',requests2.json()['msg'])

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
        if requests1.json()['msg'] ==  '打卡成功':
                print('1testcase:test_end',requests1.json()['msg'])
        elif requests1.json()['msg'] =='所在部门没有设置打卡地点':
                data1 = {
                    'deptId': '22978615332864,15189763112960,21318008938496,21420240904192,26941311627264,18851478470656,22786721398784,24623214514176,24667590250496,24721784852480,24805171810304,24846817054720,24899241660416,24946033315840,24991122083840,25040962998272,25098789867520,25147968081920,25201659367424,15818668015616,18129595719680,22670185709568',
                    'actRadius': 200,
                    'locSetName': '测试易才集团',
                    'locName': '北京市朝阳区建国路56号天洋运河F1栋',
                    'longitude': '116.518779',
                    'latitude': '39.908654'}
                r = requests.post(self.checkLocationUrl, data=json.dumps(data1), headers=self.headers)
                print('2testcase:test_end',r.status_code, 'testcase:test_start', r.json()['msg'])
                r.json()['msg'] == '考勤地点设置成功'
                requests2 = requests.post(self.url, data=json.dumps(json_param), headers=self.headers)
                print('3testcase:test_end',requests2.json()['msg'],requests2.json()['msg'].encode('utf-8'))
        else:
                print('4testcase:test_end',requests2.json()['msg'])

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
        print('1testcase:test_Outside', requests1.json()['msg'])


if __name__ == '__main__':
    unittest.main()