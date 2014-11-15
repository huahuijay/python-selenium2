#!-*- coding:utf-8 -*-

#使用相对路劲把test目录添加到path下
import sys
import unittest
import HTMLTestRunner
import time
import allcase_list


#创建测试容器
testunit=unittest.TestSuite()


#获取数组文件
alltestnames=allcase_list.caselist()

#循环读取数组中的用例
for db in alltestnames:
    testunit.addTest(unittest.makeSuite(db))


#获取现在的时间
now=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
#定义报告存放路劲
filename='D:\\Git\\PyCharm\\Develop-Python-Selenium2\\report\\'+now+'allTests.html'
fp=file(filename,'wb')

#定义测试报告
runner=HTMLTestRunner.HTMLTestRunner(
        #报告写入的文件
        stream=fp,
        #报告标题
        title=u'引入测试套件执行测试集执行用例',
        #报告的说明与描述
        description=u'用例执行情况')
# #执行测试套件
# runner=unittest.TextTestRunner()
# runner.run(testunit)

#执行用例
runner.run(testunit)


