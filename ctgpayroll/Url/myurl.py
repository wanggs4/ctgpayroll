# -*- coding:utf-8 -*-
import unittest
from ctgpayroll.myLogin.login import login

class url(object):
    def setUp(self):

        self.urlhost='https://autodiscover.ctgpayroll.com'
        '''域名'''

        self.urllogin_ios =self.urlhost+ '/ehr_saas/newMobile/login/login.mobile'
        '''IOS登录接口'''

        self.urlcheck=self.host+'/ehr_saas/web/attEmpLog/saveAttEmpLog.mobile'
        ''''saas打卡接口'''

        self.headers_Ntoken = {'Content-Type': 'application/json'}
        '''headers不带token'''

        self.headers_token = {'Content-Type': 'application/json','token':login.login_token()}
        '''headers带token'''

        self.urlcheckLocation = self.host+'/ehr_saas/web/attSetLocation/saveAttSetLocation.mobileHr'
        '''saas添加考勤地址接口'''