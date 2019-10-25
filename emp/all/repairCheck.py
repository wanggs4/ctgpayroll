
import requests,json,datetime
import unittest

class test(unittest.TestCase):


    def setUp(self):
        self.url = 'https://testapi.ctgpayroll.com/ehr_saas/web/attCheckApply/saveAttCheckApply.mobile'
        self.headers = {'Content-Type': 'application/json',
                        'token': 'vwTLTwYvBqCoKH+42+nOsY4yLktvj+CZ/L50SWKwPi46zyWMt0Vx3LMfOYY/Tzl6FBW1kZ6AeTQmqfEueTwebQ=='}

    def test_check_01(self):
        now_time = datetime.datetime.now()
        json_pqram={
            'checkTime':now_time.strftime(str,'2019-05-20 08:59:00'),
            'checkType':1,
            'remark':'测试补签上班',
            'saveType':1,
        }
        requests1 = requests.post(self.url,data=json.dumps(json_pqram),headers=self.headers)
        print('测试补签上班:test_check_01',requests1.text)

    if __name__ == '__main__':
        unittest.main()

