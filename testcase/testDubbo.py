#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests,os,sys
import unittest
import json
import logging
from commonFunctions.comFunctions import  *
from commonFunctions import dubboRunner
from commonFunctions.assertMs import appendMs
from commonFunctions.log_time_assert import logTimeAssert
class apiMain(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        logfile('DUBBO_Test.log')
        self.host=readIni('dubbo','host')
        self.port=readIni('dubbo','port')
        self.passls,self.fels=[],[]
        self.rightCode='True'

        logging.info('Initial success...')

    def test_DubboDemo(self):
        '''dubbo接口测试例子'''
        interface = 'com.dfire.soa.consumer.fe.service.IUserStatisticsFacade'  # 接口
        method = 'getByCustomerId'  # 方法
        param = {"customerId": "8afa441e596344d6862a6541567128e6"}  # 参数
        response=dubboRunner.coondoubble_data(self.host,self.port,interface,method,param)
        printlog(str_apiName=sys._getframe().f_code.co_name,str_req=None,str_res=response,str_ms=None,body=param)
        # logTimeAssert(response, sys._getframe().f_code.co_name, self.passls, self.fels, self.assertEqual, self.rightCode, param)

    @unittest.skip('final')
    def test_Z_logout(self):
        pass
    @classmethod
    def tearDownClass(cls):
        logging.info('Ending....')