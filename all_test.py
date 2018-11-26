#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
import HTMLTestRunner
import time
import threading
import sys
import os

from testcase import testMain,rewriteHtml,testDubbo
# from JimRepository.APIrequests.testcase import rewriteHtml

reload(sys)
sys.setdefaultencoding('utf-8')

def begin():
    testunit=unittest.TestSuite()
    #将测试用例加入到测试容器(套件)中
    # testunit.addTest(unittest.makeSuite(testMain.apiMain))
    testunit.addTest(unittest.makeSuite(testDubbo.apiMain))

    # filename =os.getcwd()+ '\html\\'+time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))+'API_Test.html'
    filename =os.getcwd()+ '\html\\'+time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))+'DUBBO_Test.html'

    fp = file(filename, 'wb')
    runner =HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'dubbo接口测试',
        description=u'测试用例执行情况：')
    runner.run(testunit)


# Threads=[]
# T1=threading.Thread(target=begin)
# T2=threading.Thread(target=rewriteHtml.rewrite)
# Threads.append(T1)
# Threads.append(T2)
if __name__=='__main__':
    # for t in Threads:
    #     t.setDaemon(True)
    #     t.start()
    # for t in Threads:
    #     t.join()
    begin()
    rewriteHtml.rewrite()