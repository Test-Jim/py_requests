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
import dubbo_telnet
class apiMain(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        logfile('DUBBO_Test.log')
        self.host=readIni('dubbo','host')
        self.port=readIni('dubbo','port')
        self.conn = dubbo_telnet.connect(self.host, self.port)
        self.conn.set_connect_timeout(10)
        self.conn.set_encoding('gbk')

        self.host_payCenter = readIni('dubbo', 'host_payCenter')
        self.conn_payCenter=dubbo_telnet.connect(self.host_payCenter, self.port)
        self.conn_payCenter.set_connect_timeout(10)
        self.conn_payCenter.set_encoding('gbk')

        self.host_pay = readIni('dubbo', 'host_pay')
        self.conn_pay=dubbo_telnet.connect(self.host_pay, self.port)
        self.conn_pay.set_connect_timeout(10)
        self.conn_pay.set_encoding('gbk')

        self.host_bill = readIni('dubbo', 'host_bill')
        self.conn_bill=dubbo_telnet.connect(self.host_bill, self.port)
        self.conn_bill.set_connect_timeout(10)
        self.conn_bill.set_encoding('gbk')

        self.passls, self.fels = [], []
        self.rightCode = 'True'
        logging.info('Initial success...')

    @unittest.skip('final')
    def test_ID7_1_addInst(self):
        '''企业入驻开户，添加企业担保账户'''
        interface = 'com.dfire.fin.account.service.IInstAccountService'
        method = 'addInst'
        param = {'brhName':'fanhaoyue2','linkName':'jzs','linkMobile':'15669036110'}
        command = 'invoke {0}.{1}({2},1,"jzs")'.format(interface,method,param)
        response=self.conn.do(command)
        printlog(str_apiName=sys._getframe().f_code.co_name,str_req=command,str_res=response,str_ms=None,body=param)
        self.assertEqual(True, response.get('model'))

    @unittest.skip('final')
    def test_ID8_1_addEntityBind(self):
        '''商户活动入驻开户，添加商户担保账户'''
        interface = 'com.dfire.fin.account.service.IInstAccountService'
        method = 'addEntityBind'
        param = {'brhId':'C_385449654759834895','entityId':'99929124','settleCycle':'1','settleType':'0'}
        command = 'invoke {0}.{1}({2},1,"qlgy")'.format(interface,method,param)
        response=self.conn.do(command)
        printlog(str_apiName=sys._getframe().f_code.co_name,str_req=command,str_res=response,str_ms=None,body=param)
        self.assertEqual(True, response.get('model'))

    @unittest.skip('final')
    def test_ID9_1_querySettleReconBillByPage(self):
        '''T+1活动账户机构结算单报表查询'''
        interface = 'com.dfire.fin.account.service.ISettleBillService'
        method = 'querySettleReconBillByPage'
        param = {'billDateBegin':'20181118','billDateEnd':'20181207','accountNo':'385449654759834896','brhId':'C_385449654759834895','accountType':'008'}
        command = 'invoke {0}.{1}({2})'.format(interface,method,param)
        response=self.conn.do(command)
        printlog(str_apiName=sys._getframe().f_code.co_name,str_req=command,str_res=response,str_ms=None,body=param)
        self.assertEqual(True, response.get('model'))

    @unittest.skip('final')
    def test_ID12_1_checkAccountExist(self):
        '''是否开通了相关账户接口 查机构'''
        interface = 'com.dfire.fin.account.service.IInstAccountService'
        method = 'checkAccountExist'
        param = ('C_385449654759834895','008')
        command = 'invoke {0}.{1}("{2[0]}","{2[1]}")'.format(interface,method,param)
        response=self.conn.do(command)
        printlog(str_apiName=sys._getframe().f_code.co_name,str_req=command,str_res=response,str_ms=None,body=param)
        self.assertEqual(True, response.get('model'))

    @unittest.skip('final')
    def test_ID12_2_checkAccountExist(self):
        '''是否开通了相关账户接口 查商家'''
        interface = 'com.dfire.fin.account.service.IInstAccountService'
        method = 'checkAccountExist'
        param = ('99929124','003')
        command = 'invoke {0}.{1}("{2[0]}","{2[1]}")'.format(interface,method,param)
        response=self.conn.do(command)
        printlog(str_apiName=sys._getframe().f_code.co_name,str_req=command,str_res=response,str_ms=None,body=param)
        self.assertEqual(True, response.get('model'))

    @unittest.skip('final')
    def test_ID13_1_queryActivityInstList(self):
        ''' 查询营销平台机构列表'''
        interface = 'com.dfire.fin.account.service.IInstAccountService'
        method = 'queryActivityInstList'
        param = {'brhId':'99929124','accountNo':'385449654759834909','brhType':'01'}
        command = 'invoke {0}.{1}({2})'.format(interface,method,param)
        response=self.conn.do(command)
        printlog(str_apiName=sys._getframe().f_code.co_name,str_req=command,str_res=response,str_ms=None,body=param)
        self.assertEqual(True, response.get('model'))

    @unittest.skip('final')
    def test_ID14_1_queryEntityList(self):
        ''' 查询商户管理接口'''
        interface = 'com.dfire.fin.account.service.IInstAccountService'
        method = 'queryEntityList'
        param = {'entityId':'99929124','accoutnNo':'385449654759834909'}
        command = 'invoke {0}.{1}({2})'.format(interface,method,param)
        response=self.conn.do(command)
        printlog(str_apiName=sys._getframe().f_code.co_name,str_req=command,str_res=response,str_ms=None,body=param)
        self.assertEqual(True, response.get('model'))

    @unittest.skip('final')
    def test_ID15_1_setEnableWithDraw(self):
        ''' 设置是否允许提现'''
        interface = 'com.dfire.fin.account.service.IInstAccountService'
        method = 'setEnableWithDraw'
        param = ('99929124','true')
        command = 'invoke {0}.{1}("{2[0]}","{2[1]}")'.format(interface,method,param)
        response=self.conn.do(command)
        printlog(str_apiName=sys._getframe().f_code.co_name,str_req=command,str_res=response,str_ms=None,body=param)
        self.assertEqual(True, response.get('model'))

    @unittest.skip('final')
    def test_PayCenterID1_1_barpay(self):
        '''条码支付,都正确'''
        interface = 'com.dfire.pay.center.service.payment.IPaymentService'
        method = 'barpay'
        param = {"authCode":"134747490157949686","guarantee":'true',"managerReceive":'false',"messageTag":"wechat_bar_pay","payClientType":"WECHAT","payOrder":
                {"allOrderId":"99227185dEw8yhBgAiNbUXqezbIMCQ","customerRegisterId":"cb0d3f29b248452f98969db6af70758c","entityId":"99929124","needPayFee":15,
                "openId":"2088002036458655","orderId":"99227185dEw8yhBgAiNbUXqezbIMCQ","originFee":15,"prePay":'false',"timeout":60,"title":"Test"},
                "paySource":"CASHIER","remoteAddr":"10.1.12.3","tradeFeeRate":0.1,"unDiscountableAmount":0,"useAlipayDiscount":'true'}
        command = 'invoke {0}.{1}({2})'.format(interface,method,param)
        response=self.conn_payCenter.do(command)
        printlog(str_apiName=sys._getframe().f_code.co_name,str_req=command,str_res=response,str_ms=None,body=param)
        self.assertEqual(None,response.get('model'))


    def test_Q1_guaranteeALLINConfirmPayment(self):
        '''通联担保支付确认接口(billing)'''
        interface = 'com.dfire.paybill.service.IGuaranteePaymentService'
        method = 'guaranteeALLINConfirmPayment'
        param =('C_385449654759834895' ,'99929124', '99929124T000386816295619940082','15', '2')
        command = 'invoke {0}.{1}("{2[0]}","{2[1]}","{2[2]}",{2[3]},{2[4]})'.format(interface,method,param)
        response=self.conn_bill.do(command)
        printlog(str_apiName=sys._getframe().f_code.co_name,str_req=command,str_res=response,str_ms=None,body=param)
        self.assertEqual(None,response.get('model'))

    @unittest.skip('final')
    def test_Q2_guaranteeALLINConfirmPayment(self):
        '''通联担保支付确认接口(billing)'''
        interface = 'com.dfire.paybill.service.IGuaranteePaymentService'
        method = 'guaranteeALLINConfirmPayment'
        param =('C_385061656285299356' ,'99935448', '99935448T000386816295619940043','10', '0')
        command = 'invoke {0}.{1}("{2[0]}","{2[1]}","{2[2]}",{2[3]},{2[4]})'.format(interface,method,param)
        response=self.conn_bill.do(command)
        printlog(str_apiName=sys._getframe().f_code.co_name,str_req=command,str_res=response,str_ms=None,body=param)
        self.assertEqual(None,response.get('model'))

    @unittest.skip('final')
    def test_PayID4_1_getByOutTradeNo(self):
        '''根据交易号查询支付流水'''
        interface = 'com.dfire.pay.bill.service.IPayBillReadService'
        method = 'getByOutTradeNo'
        param = ('99929124','99929124T000385457127797443689')
        command = 'invoke {0}.{1}("{2[0]}","{2[1]}")'.format(interface,method,param)
        response=self.conn_pay.do(command)
        printlog(str_apiName=sys._getframe().f_code.co_name,str_req=command,str_res=response,str_ms=None,body=param)
        self.assertEqual(None,response.get('model'))

    @unittest.skip('final')
    def test_PayCenterID5_1_getMerchantAuthInfoBaseByEntityId(self):
        '''获取支付信息'''
        interface = 'com.dfire.pay.center.service.settings.IMerchantAuthService'
        method = 'getMerchantAuthInfoBaseByEntityId'
        param = ('99929124','false')
        command = 'invoke {0}.{1}("{2[0]}","{2[1]}")'.format(interface,method,param)
        response=self.conn_payCenter.do(command)
        printlog(str_apiName=sys._getframe().f_code.co_name,str_req=command,str_res=response,str_ms=None,body=param)
        self.assertEqual(None,response.get('model'))

    @unittest.skip('final')
    def test_PayID4_1_guaranteeConfirmPaySucc(self):
        '''	确认支付附加费回流'''
        interface = 'com.dfire.pay.bill.service.IPayBillWriteService'
        method = 'guaranteeConfirmPaySucc'
        param = ('99929124','99929124T000385457127797443689','0.01','0.008','20180101','0')
        command = 'invoke {0}.{1}("{2[0]}","{2[1]}",{2[2]},{2[3]},"{2[4]}",{2[5]})'.format(interface,method,param)
        response=self.conn_pay.do(command)
        printlog(str_apiName=sys._getframe().f_code.co_name,str_req=command,str_res=response,str_ms=None,body=param)
        self.assertEqual(None,response.get('model'))





    @classmethod
    def tearDownClass(cls):
        logging.info('Ending....')