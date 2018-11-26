from comFunctions import apims,printlog
from assertMs import appendMs
from unittest import TestCase
def logTimeAssert(response,apiname,passls,fels,func,rightcode,body=None):
    ms = str(apims(response))
    printlog(apiname, response.url, response.text, str_ms=ms,body=body)
    appendMs(response, ms, passls, fels)
    func(rightcode,response.json()['code'])

# def logTimeAssert_Dubbo(response,apiname,passls,fels,func,rightcode,param):
#     printlog(apiname, 'URL', response, str_ms=ms,body=param)
#     appendMs(response, ms, passls, fels)
#     func(rightcode,response.json()['success'])