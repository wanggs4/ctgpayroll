# coding:utf-8
import requests,json
import unittest
import casemethod.method


class MyTestSuite(unittest.TestCase):
    def setUp(self):
        self.url = 'https://autodiscover.ctgpayroll.com/ehr_saas/newMobile/testLogin/testLogin.mobile'
        self.headers = {'Content-Type': 'application/json'}
        self.checkLocationUrl = 'https://autodiscover.ctgpayroll.com/ehr_saas/web/attEmpLog/saveAttEmpLog.mobile'

    def test_login(self):
        json_login = {
            'custId': 15921595797504,
            'deviceId': '8B39DD16-3442-43DE-959D-0EE9CD0C1EE6',
            'mobile': 18612533709,
            'verificationCode': 4321
        }
        login = requests.post(self.url,data=json.dumps(json_login),headers=self.headers)
        print(login.status_code, 'testcase:testLogin', login.json()['msg'])
        print(login)



if __name__ == '__main__':
    unittest.main(testLoader=casemethod.method.SequentialTestLoader())



