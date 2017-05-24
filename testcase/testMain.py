#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests,os,sys
import unittest
import logging
from commonFunctions.comFunctions import  *

class apiMain(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        logfile('API_Test.log')
        self.url=readIni('host','apihost')
        self.headers={'Accept':'device_key=890& version=1.1.1&client_type=mobile_ios&client_os_version=10.0.0'}
        self.token=[]
        self.passls,self.fels=[],[]
        self.session=requests.Session()

        logging.info('Initial success...')



    def test_A_login(self):
        '''登录'''
        apiname,url='test_A_login','login'
        body={'mobile':'15669036110',
              'password':'zzzzzz',
              'code':'1334'}
        response=self.session.post(url=self.url+url,data=body,headers=self.headers)
        self.token.append(response.json()['data']['token'])

        ms=str(apims(response))
        printlog(apiname,str(body),response.text,ms)
        try:
            if response.json()['code']==0:
                self.passls.append(ms)
            else:
               self.fels.append(ms)
        except:
            self.fels.append(ms)
        self.assertEqual(0,response.json()['code'])
        return response
    # def test_B_getCompany(self):
    #     '''获取企业信息'''
    #     apiname,url='test_B_getCompany','company/company_info'
    #     body={'token':self.token[0]}
    #     logging.info(self.session.cookies)
    #     response=self.session.get(url=self.url+url,params=body,headers=self.headers)
    #     ms=str(apims(response))
    #     printlog(apiname,response.url,response.text,ms)
    #     try:
    #         if response.json()['code']==0:
    #             self.passls.append(ms)
    #         else:
    #            self.fels.append(ms)
    #     except:
    #         self.fels.append(ms)
    #     self.assertEqual(0,response.json()['code'])
    # def test_C_getDealerDetial(self):
    #     '''获取商家信息'''
    #     apiname,url='test_C_getDealerDetial','dealer/detail'
    #     body={'token':self.token[0],
    #           'dealer_id':1}
    #     response=self.session.get(url=self.url+url,params=body)
    #     ms=str(apims(response))
    #     printlog(apiname,response.url,response.text,ms)
    #     try:
    #         if response.json()['code']==0:
    #             self.passls.append(ms)
    #         else:
    #            self.fels.append(ms)
    #     except:
    #         self.fels.append(ms)
    #     self.assertEqual(0,response.json()['code'])
    #
    # def test_D_upload(self):
    #     '''客户端上传图片初始化token'''
    #     apiname,url='test_D_upload','qiniu/get_token'
    #     file={'type':(open(sys.path[0]+'\\testcase\pictures\p1.png','rb'),'image/png')}
    #     response=self.session.post(url=self.url+url,files=file)
    #     # self.token.append(response.json()['data']['token'])
    #
    #     ms=str(apims(response))
    #     printlog(apiname,str(file),response.text,ms)
    #     try:
    #         if response.json()['code']==0:
    #             self.passls.append(ms)
    #         else:
    #            self.fels.append(ms)
    #     except:
    #         self.fels.append(ms)
    #     self.assertEqual(0,response.json()['code'])
    #
    # def test_E_charge_brand_list(self):
    #     '''主营品牌筛选接口'''
    #     apiname,url='test_E_charge_brand_list','car/charge_brand_list'
    #     response=self.session.get(url=self.url+url,headers=self.headers)
    #
    #     body={}
    #     ms=str(apims(response))
    #
    #     printlog(apiname,str(body),response.text,ms)
    #     try:
    #         if response.json()['code']==0:
    #             self.passls.append(ms)
    #         else:
    #            self.fels.append(ms)
    #     except:
    #         self.fels.append(ms)
    #     self.assertEqual(0,response.json()['code'])

    @classmethod
    def tearDownClass(cls):
        logging.info('Ending....')
