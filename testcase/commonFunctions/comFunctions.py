import logging
import os
import ConfigParser


def apims(response):
    return str(response.elapsed.microseconds/1000)+'ms'

def logfile(filename):
    # now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    logfilename=os.getcwd()+'\logs\\'+filename
    logging.basicConfig(level=logging.INFO,
            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
            datefmt='%a, %d %b %Y %H:%M:%S',
            filename=logfilename,
            )
def printlog(str_apiName,str_req,str_res,str_ms=None,body=None):
    logging.info(str_apiName+' requestUrl:'+str_req)
    logging.info('body:'+str(body))
    # str_res=str_res.decode('unicode-escape')
    str_res=str_res.decode('UTF-8')

    logging.info(str_apiName+' APItime:'+str_ms+' response:'+str_res)
    logging.info('-----------------------------------------------------')

def readIni(key,value):
    ini=ConfigParser.ConfigParser()
    inipath=os.getcwd()+'\\apiMain.ini'
    ini.read(inipath)
    end=ini.get(key,value)
    return  end

