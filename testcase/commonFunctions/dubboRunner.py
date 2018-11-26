# -*- coding: utf-8 -*-
import dubbo_telnet
def coondoubble_data(Host,Port,interface,method,param):
    # 初始化dubbo对象
    conn = dubbo_telnet.connect(Host, Port)
    # 设置telnet连接超时时间
    conn.set_connect_timeout(10)
    # 设置dubbo服务返回响应的编码
    conn.set_encoding('gbk')
    # conn.invoke(interface, method, param)
    command = 'invoke %s.%s(%s)'%(interface,method,param)
    return  conn.do(command)