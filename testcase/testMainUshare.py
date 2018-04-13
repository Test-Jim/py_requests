#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests,os,sys
import unittest
import json
import logging
from commonFunctions.comFunctions import  *
from commonFunctions.assertMs import appendMs
from commonFunctions.log_time_assert import logTimeAssert
class apiMain(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        logfile('API_Test.log')
        self.url=readIni('host','apihost')
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
                      }
        self.passls,self.fels=[],[]
        self.session=requests.Session()
        self.auth_token=[]
        self.rightCode,self.cellPhone,self.password='100','18888888887','123456'
        logging.info('Initial success...')

    def test_A_login(self):
        '''登录友奢'''
        # apiname,url=sys._getframe().f_code.co_name,'mng/doLogin.json?loginId=%s&loginPassword=%s'%(self.cellPhone,self.password)
        apiname,url=sys._getframe().f_code.co_name,'mng/doLogin.json'
        body={'loginId':self.cellPhone,
              'loginPassword': self.password}
        # body = json.dumps(body)
        response=self.session.post(url=self.url+url,data=body,headers=self.headers)
        logTimeAssert(response, apiname, self.passls, self.fels, self.assertEqual, self.rightCode,body)


    def test_B1_merchants(self):
        '''商户列表筛选(查询全部)'''
        apiname,url=sys._getframe().f_code.co_name,'mng/merchant/merchantList.json'
        body={'page':1,
              'pageSize':20
              }
        # body = json.dumps(body)
        response=self.session.get(url=self.url+url,params=body,headers=self.headers)
        logTimeAssert(response, apiname, self.passls, self.fels, self.assertEqual, self.rightCode,body)


    def test_B2_add_merchant(self):
        '''保存商户信息'''
        apiname,url=sys._getframe().f_code.co_name,'mng/merchant/save.json'
        body={'uniformSocialCreditCode':'111111111111111111',
              'salesId':'金大大',
              'province':'北京',
              'merchantStatus':'init',
              'merchantName':'金大大集团',
              'merchantContact':'金大大',
              'merchantCode':'5555',
              'isCertnoThreeInOne':1,
              'institutionalCreditCode':'2222222222222222222',
              'feeRate' :5,
              'corporationPhoneNo':'15669036110',
              'corporationName':'金大大',
              'contractEndTime':'2019-02-28',
              'contractBeginTime':'2018-01-11',
              'contactPhoneNo':'15669036110',
              'commonImages':[{"imageBizType": "4", "imageFilePath": "/d56613b6-7573-45da-a25e-48be8fb5024c.jpg"}, {
                                "imageBizType": "5", "imageFilePath": "/d56613b6-7573-45da-a25e-48be8fb5024c.jpg"}, {
                                "imageBizType": "6", "imageFilePath": "/d56613b6-7573-45da-a25e-48be8fb5024c.jpg"}, {
                                "imageBizType": "7", "imageFilePath": "/d56613b6-7573-45da-a25e-48be8fb5024c.jpg"}, {
                                "imageBizType": "8", "imageFilePath": "/d56613b6-7573-45da-a25e-48be8fb5024c.jpg"}, {
                                "imageBizType": "9", "imageFilePath": "/d56613b6-7573-45da-a25e-48be8fb5024c.jpg"}, {
                                "imageBizType": "10", "imageFilePath": "/d56613b6-7573-45da-a25e-48be8fb5024c.jpg"}, {
                                "imageBizType": "1", "imageFilePath": "/d56613b6-7573-45da-a25e-48be8fb5024c.jpg"}],
              'city':'北京',
              'cashDeposit':'1999',
              'businessLicense':'444444444444444444',
              'businessAddress' :'北京, 北京, 东城区',
              'bankAccOpenLicense': '23333333333333',
              'area':'东城区',
              'address':'地方豆腐干反对斯蒂芬'
              }
        # body = json.dumps(body)
        response=self.session.post(url=self.url+url,data=body)
        logTimeAssert(response, apiname, self.passls, self.fels, self.assertEqual, self.rightCode,body)


    def test_B_merchant(self):
        '''查询商户信息'''
        apiname,url=sys._getframe().f_code.co_name,'mng/merchant/merchantById.json'
        body={'merchantCode':1342,
              }
        response=self.session.get(url=self.url+url,params=body,headers=self.headers)
        logTimeAssert(response, apiname, self.passls, self.fels, self.assertEqual, self.rightCode,body)


    @unittest.skip('final')
    def test_Z_logout(self):
        pass
    @classmethod
    def tearDownClass(cls):
        logging.info('Ending....')