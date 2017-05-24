#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os,re,time,logging
from bs4 import BeautifulSoup
from testcase import testMain
def rewrite():
    #这个时间很重要，必须大于所有接口运行累加的时间
    time.sleep(1)

    result_dir=os.path.abspath('')+"\html\\"
    l=os.listdir(result_dir)
    l.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn) if not os.path.isdir(result_dir+"\\"+fn) else 0)
    with open(result_dir+l[-1],'r+') \
        as fd:
            soup=BeautifulSoup(fd,'lxml')
            passls,fels=testMain.apiMain.passls,testMain.apiMain.fels
            listpass=soup.find_all('td',colspan='5',text=True)
            listfe=soup.find_all('a',class_="popup_link")

            if len(passls)==len(listpass):
                for index in range(len(passls)):
                    listpass[index].string=listpass[index].string+'['+passls[index]+']'
            else:
                logging.error(' length:'+str(len(passls))+'!= '+str(len(listpass)))
            if len(fels)==len(listfe):
                for index in range(len(fels)):
                    listfe[index].string=listfe[index].string+'['+fels[index]+']'
            else:
                logging.error(' length:'+str(len(fels))+'!= '+str(len(listfe)))
            fd.seek(0,os.SEEK_SET)#移动到文件头,目的是为了下次依旧可以从文件头开始操作文件
            fd.write(str(soup))#重写整个文件
            fd.close()