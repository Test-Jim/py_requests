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
        self.url_2=readIni('host','apihost_2')
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
        self.passls,self.fels=[],[]
        self.session=requests.Session()
        self.auth_token=[]
        self.rightCode,self.cellPhone,self.systemID='200','17788551914',1
        logging.info('Initial success...')

    def test_A_getVerifycode(self):
        '''获取手机验证码'''
        apiname,url=sys._getframe().f_code.co_name,'lc-sso-web/sso/rest/get/verifycode'
        body={'cellphone':self.cellPhone,
              'systemId': self.systemID}
        response=self.session.get(url=self.url+url,params=body,headers=self.headers)
        logTimeAssert(response, apiname, self.passls, self.fels, self.assertEqual, self.rightCode,body)

    def test_B_getSystems(self):
        '''获取已经注册的系统信息'''
        apiname,url=sys._getframe().f_code.co_name,'lc-sso-web/sso/rest/get/systems'
        body={}
        response=self.session.get(url=self.url+url,params=body,headers=self.headers)
        logTimeAssert(response,apiname,self.passls,self.fels,self.assertEqual,self.rightCode)

    @unittest.skip('final')
    def test_C_pwdApply(self):
        '''申请临时密码'''
        apiname,url=sys._getframe().f_code.co_name,'lc-sso-web/sso/rest/pwd/apply'
        body={'cellphone':self.cellPhone,
              'systemId': self.systemID}
        response=self.session.post(url=self.url+url,params=body,headers=self.headers)
        logTimeAssert(response, apiname, self.passls, self.fels, self.assertEqual, self.rightCode,body)

    def test_D_rememberme(self):
        '''记住登录用户名'''
        apiname,url=sys._getframe().f_code.co_name,'lc-sso-web/sso/rest/rememberme'
        body={'cellphone':self.cellPhone,
              'checked': 'false'}
        response=self.session.post(url=self.url+url,params=body,headers=self.headers)
        logTimeAssert(response, apiname, self.passls, self.fels, self.assertEqual, self.rightCode,body)

    def test_E_login(self):
        '''登录'''
        apiname,url=sys._getframe().f_code.co_name,'lc-sso-web/sso/rest/code/dologin'
        body={'cellphone':self.cellPhone,
              'verifycode':'888888',
              'systemId':self.systemID,
              'redirectURL':''}
        response=self.session.post(url=self.url+url,data=body,headers=self.headers)
        self.auth_token.append(response.json()['data']['auth_token'])
        # logging.info(self.auth_token)
        logTimeAssert(response, apiname, self.passls, self.fels, self.assertEqual, self.rightCode,body)

    def test_F_loginuserInfo(self):
        '''获取登录用户信息'''
        apiname,url=sys._getframe().f_code.co_name,'lc-sso-web/sso/api/auth/loginuserInfo'
        body={}
        response=self.session.get(url=self.url+url,params=body,headers=self.headers)
        logTimeAssert(response, apiname, self.passls, self.fels, self.assertEqual, self.rightCode,body)
        if response.json()['data']['phoneNumber']==self.cellPhone:
            global idUser
            idUser=response.json()['data']['userId']

    def test_G_systemInfo(self):
        '''指定系统分配的菜单树及菜单下的功能'''
        apiname,url=sys._getframe().f_code.co_name,'lc-sso-web/sso/api/auth/menufunction'
        body={'systemId':self.systemID}
        response=self.session.get(url=self.url+url,params=body,headers=self.headers)
        logTimeAssert(response, apiname, self.passls, self.fels, self.assertEqual, self.rightCode,body)

    def test_H1_addDepart(self):
        '''新增部门'''
        apiname,url=sys._getframe().f_code.co_name,'lc-ams-web/api/ams/departments?auth_token=%s'%self.auth_token[0]
        body={'companyId':'1',
              'flag':'1',
              'name':u'运营测试部门',
              'parentId':'0',
              }
        body = json.dumps(body)
        response=self.session.post(url=self.url_2+url,data=body,headers={'Content-Type': 'application/json'})
        logging.info(response.cookies)
        logTimeAssert(response, apiname, self.passls, self.fels, self.assertEqual, self.rightCode,body)

    def test_H2_findDepart(self):
        '''查找所有部门'''
        apiname,url=sys._getframe().f_code.co_name,'lc-ams-web/api/ams/departments'
        body={}
        response=self.session.get(url=self.url_2+url,params=body,headers=self.headers)
        logTimeAssert(response, apiname, self.passls, self.fels, self.assertEqual, self.rightCode,body)
        for index in response.json()['data']:
            if index['name']==u'运营测试部门':
                global idNumber
                idNumber=index['id']

    def test_H3_upDepart(self):
        '''更新部门'''
        apiname,url=sys._getframe().f_code.co_name,'lc-ams-web/api/ams/departments/%s/update'%(idNumber)
        body={'companyId':'1',
                'flag':'1',
                'name':u'运营测试部门更新',
                'parentId':'0'}
        body = json.dumps(body)
        response=self.session.post(url=self.url_2+url,data=body,headers={'Content-Type': 'application/json'})
        logTimeAssert(response, apiname, self.passls, self.fels, self.assertEqual, self.rightCode,body)

    def test_H4_delDepart(self):
        '''删除部门'''
        apiname,url=sys._getframe().f_code.co_name,'lc-ams-web/api/ams/departments/%s/delete'%(idNumber)
        body={'id':idNumber,
              'auth_token':self.auth_token[0]
              }
        response=self.session.post(url=self.url_2+url,data=body,headers={'Content-Type': 'application/json'})
        logTimeAssert(response, apiname, self.passls, self.fels, self.assertEqual, self.rightCode,body)

    def test_I1_addDomain(self):
        '''新增域名'''
        apiname,url=sys._getframe().f_code.co_name,'lc-ams-web/api/ams/domains'
        body={'description':u'测试域名',
              'flag':'1',
              'name':'www.test.com',
              'isDisplay':0}
        body = json.dumps(body)
        response=self.session.post(url=self.url_2+url,data=body,headers={'Content-Type': 'application/json'})
        logTimeAssert(response, apiname, self.passls, self.fels, self.assertEqual, self.rightCode,body)

    def test_I2_getDomain(self):
        '''根据ID获取域名信息'''
        apiname,url=sys._getframe().f_code.co_name,'lc-ams-web/api/ams/domain/1'
        body={}
        response=self.session.get(url=self.url_2+url,params=body,headers=self.headers)
        logTimeAssert(response, apiname, self.passls, self.fels, self.assertEqual, self.rightCode,body)

    def test_I3_getAllDomain(self):
        '''获取所有域名信息'''
        apiname,url=sys._getframe().f_code.co_name,'lc-ams-web/api/ams/domains'
        body={}
        response=self.session.get(url=self.url_2+url,params=body,headers=self.headers)
        logTimeAssert(response, apiname, self.passls, self.fels, self.assertEqual, self.rightCode,body)
        for index in response.json()['data']:
            if index['name']=='www.test.com':
                global idDomain
                idDomain=index['id']

    def test_I4_upDomain(self):
        '''更新域名'''
        apiname, url = sys._getframe().f_code.co_name, 'lc-ams-web/api/ams/domains/%s/update'%idDomain
        body={'description':u'测试域名更新',
              'flag':'1',
              'name':'www.testupdate.com',
              'isDisplay':0}
        body = json.dumps(body)
        response=self.session.post(url=self.url_2+url,data=body,headers={'Content-Type': 'application/json'})
        logTimeAssert(response, apiname, self.passls, self.fels, self.assertEqual, self.rightCode,body)

    def test_I5_delDepart(self):
        '''删除域名'''
        apiname,url=sys._getframe().f_code.co_name,'lc-ams-web/api/ams/domains/%s/delete'%idDomain
        body={'id':idDomain}
        response=self.session.post(url=self.url_2+url,data=body,headers={'Content-Type': 'application/json'})
        logTimeAssert(response, apiname, self.passls, self.fels, self.assertEqual, self.rightCode,body)

    def test_J1_addEmployee(self):
        '''新增员工'''
        apiname, url = sys._getframe().f_code.co_name, 'lc-ams-web/api/ams/employees'
        body={'departmentId':'40',
              'email':"test@91licheng.cn",
              'flag':'1',
              'hiredate':"2017-09-15 00:00:00",
              'name':'新测试员工',
              'phoneNumber':"15555555555",
              'qq':"333333333",
              'sex':'0',
              'wechat':"333333333",
              'workNumber':"666666",
              'workingStatus':'1'}
        body=json.dumps(body)
        response=self.session.post(url=self.url_2+url,data=body,headers={'Content-Type': 'application/json'})
        logTimeAssert(response, apiname, self.passls, self.fels, self.assertEqual, self.rightCode,body)

    def test_J2_getAllImages(self):
        '''获取系统默认头像'''
        apiname, url = sys._getframe().f_code.co_name, 'lc-ams-web/api/ams/employees/allImagePath'
        body={}
        response=self.session.get(url=self.url_2+url,params=body,headers=self.headers)
        logTimeAssert(response, apiname, self.passls, self.fels, self.assertEqual, self.rightCode,body)

    def test_J3_getEmpNumber(self):
        '''获取部门人数统计信息'''
        apiname, url = sys._getframe().f_code.co_name, 'lc-ams-web/api/ams/employees/countEmpOfDept'
        body={'deptId':'40'}
        response=self.session.get(url=self.url_2+url,params=body,headers=self.headers)
        logTimeAssert(response, apiname, self.passls, self.fels, self.assertEqual, self.rightCode,body)

    def test_J4_upImage(self):
        '''修改员工头像'''
        apiname, url = sys._getframe().f_code.co_name, 'lc-ams-web/api/ams/employees/updateImage'
        body={'image':'1',
              'userId':idUser}
        logging.info(idUser)
        response=self.session.post(url=self.url_2+url,data=body,headers=self.headers)
        logTimeAssert(response, apiname, self.passls, self.fels, self.assertEqual, self.rightCode,body)

    def test_J5_getAllEmp(self):
        '''获取所有员工信息'''
        apiname, url = sys._getframe().f_code.co_name, 'lc-ams-web/api/ams/employees'
        body={}
        response=self.session.get(url=self.url_2+url,params=body,headers=self.headers)
        logTimeAssert(response, apiname, self.passls, self.fels, self.assertEqual, self.rightCode,body)
        for index in response.json()['data']:
            if index['name']==u'新测试员工':
                global idEmp
                idEmp=index['id']

    def test_J6_upEmp(self):
        '''更新员工信息'''
        apiname, url = sys._getframe().f_code.co_name, 'lc-ams-web/api/ams/employees/%s/update'%idEmp
        body={'departmentId':'40',
              'email':"test@91licheng.cn",
              'flag':'1',
              'hiredate':"2017-09-15 00:00:00",
              'name':'新测试员工123',
              'phoneNumber':"15555555555",
              'qq':"333333333",
              'sex':'0',
              'wechat':"333333333",
              'workNumber':"666666",
              'workingStatus':'1'}
        body=json.dumps(body)
        response=self.session.post(url=self.url_2+url,data=body,headers={'Content-Type': 'application/json'})
        logTimeAssert(response, apiname, self.passls, self.fels, self.assertEqual, self.rightCode,body)

    def test_J7_delEmp(self):
        '''删除员工'''
        apiname, url = sys._getframe().f_code.co_name, 'lc-ams-web/api/ams/employees/%s/delete'%idEmp
        body={}
        response=self.session.post(url=self.url_2+url,data=body,headers=self.headers)
        logTimeAssert(response, apiname, self.passls, self.fels, self.assertEqual, self.rightCode,body)

    def test_K_getLog(self):
        '''分页查询操作日志'''
        apiname, url = sys._getframe().f_code.co_name, 'lc-ams-web/api/ams/operateLogs/1/10'
        body={"action": "1",
              "endTime": "2017-10-18",
              "startTime": "2017-10-03",
              "userName": ""}
        body=json.dumps(body)
        response=self.session.post(url=self.url_2+url,data=body,headers={'Content-Type': 'application/json'})
        logTimeAssert(response, apiname, self.passls, self.fels, self.assertEqual, self.rightCode,body)

    def test_L1_addSystem(self):
        '''添加系统'''
        apiname, url = sys._getframe().f_code.co_name, 'lc-ams-web/api/ams/systems'
        body={
              "companyId": 1,
              "description": "测试系统",
              "domainId": "4",
              "name": "测试系统",
              "type": "1",
              "url": self.url+'lc-ams-web/api'
            }
        body=json.dumps(body)
        response=self.session.post(url=self.url_2+url,data=body,headers={'Content-Type': 'application/json'})
        logTimeAssert(response, apiname, self.passls, self.fels, self.assertEqual, self.rightCode,body)

    def test_L2_getAllSystem(self):
        '''获取所有系统'''
        apiname, url = sys._getframe().f_code.co_name, 'lc-ams-web/api/ams/systems'
        body={}
        response=self.session.get(url=self.url_2+url,params=body)
        logTimeAssert(response, apiname, self.passls, self.fels, self.assertEqual, self.rightCode,body)
        for index in response.json()['data']:
            if index['name']=='测试系统':
                global systemid
                systemid=index['id']

    def test_L3_getOneSystem(self):
        '''获取单个系统'''
        apiname, url = sys._getframe().f_code.co_name, 'lc-ams-web/api/ams/systems/'
        body={'id':systemid}
        response=self.session.get(url=self.url_2+url,params=body)
        logTimeAssert(response, apiname, self.passls, self.fels, self.assertEqual, self.rightCode,body)

    def test_L4_upSystem(self):
        '''更新系统'''
        apiname, url = sys._getframe().f_code.co_name, 'lc-ams-web/api/ams/systems/%s/update'%systemid
        body={
              "companyId": 1,
              "description": "测试系统更新",
              "domainId": "4",
              "name": "测试系统",
              "type": "1",
              "url": self.url+'lc-ams-web/api'
            }
        body=json.dumps(body)
        response=self.session.post(url=self.url_2+url,data=body,headers={'Content-Type': 'application/json'})
        logTimeAssert(response, apiname, self.passls, self.fels, self.assertEqual, self.rightCode,body)

    def test_L4_1_Addrole(self):
        '''添加角色'''
        apiname, url = sys._getframe().f_code.co_name, 'lc-ams-web/api/ams/roles'
        body={
                "adminFlag": 0,
                "description": "测试角色描述",
                "name": "测试角色",
                "systemId": systemid
            }
        body=json.dumps(body)
        response=self.session.post(url=self.url_2+url,data=body,headers={'Content-Type': 'application/json'})
        logTimeAssert(response, apiname, self.passls, self.fels, self.assertEqual, self.rightCode,body)

    def test_L4_2_GetAllroles(self):
        pass
    def test_L4_3_GetOneRole(self):
        pass
    def test_L4_4_GetRoleMenu(self):
        pass
    @unittest.skip('角色操作完后再删除系统')
    def test_L5_deldeteSystem(self):
        '''删除系统'''
        apiname, url = sys._getframe().f_code.co_name, 'lc-ams-web/api/ams/systems/%s/delete'%systemid
        body={'id':systemid}
        response=self.session.post(url=self.url_2+url,data=body)
        logTimeAssert(response, apiname, self.passls, self.fels, self.assertEqual, self.rightCode,body)


    @unittest.skip('final')
    def test_Z_logout(self):
        pass
    @classmethod
    def tearDownClass(cls):
        logging.info('Ending....')