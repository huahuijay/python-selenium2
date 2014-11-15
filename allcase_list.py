#!-*- coding:utf-8 -*-
'''
作者：无涯
方法描述：用例集设置成数组的形式读取
完成时间：2014-09-08 20:55:21
'''
import sys
sys.path.append("\test_case")
from test_case import *

#用例文件列表
def caselist():
    alltestnames=[
        Assertions.Assertions,
        baidu.Baidu]
    print "success read case list!"

    return alltestnames