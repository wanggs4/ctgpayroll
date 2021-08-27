# -*- coding:utf-8 -*-
import requests,json
import unittest
from ctgpayroll.MyUrl.myurl import *


class login(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testlogin_token(self):
        json_param = {
            'custId': '15921595797504',
            'deviceId': '8B39DD16-3442-43DE-959D-0EE9CD0C1EE6',
            'mobile': '18612533709',
            'verificationCode': '4321'}
        r = requests.post (url.urllogin_ios(),data=json.dumps (json_param), headers=url.headers_Ntoken)
        return r.json ( )['result']['data']['token']
        print(r.json()['msg'])