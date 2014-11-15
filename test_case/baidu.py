#!-*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import unittest,time,re,os,time
#引入HTMLTestRunner包
import HTMLTestRunner
import baidu

#导入公共的类
from package import common
from package import user_info
from package import resource


class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.base_url='http://www.baidu.com'
        #脚本运行时，错误的信息将打印到这个列表中
        self.verificationErrors=[]
        #是否接受下一个A警告
        self.accept_next_alert=True

    def testBaidu(self):
        '''百度测试'''
        driver=self.driver
        driver.get(self.base_url+'/')
        #断言来判断title是否正确
        try:
            self.assertEqual(u'百度一下，你就知道',driver.title)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def testVke(self):
        driver=self.driver
        driver.get('http://www.baidu.com')
        common.findID(driver,'kw').send_keys('webdriver')

    def testClick(self):
        driver=self.driver
        driver.get('http://www.baidu.com')
        common.findID(driver,'kw').send_keys('webdriver')
        common.findID(driver,'su').click()

    def testUser_Info(self):
        driver=self.driver
        driver.get('http://www.baidu.com')
        common.findID(driver,user_info.soID).send_keys('webdriver')
        common.findID(driver,user_info.clickID).click()
        time.sleep(3)

    def testInputName(self):
        driver=self.driver
        driver.get('http://my.weke.com/login.html')
        driver.find_element_by_class_name('login-btn').click()
        text=driver.find_element_by_xpath('html/body/div[1]/div[2]/div[2]/div/div[2]').text
        if text==resource.inputName:
            print '测试通过'
        else:
            print '提示信息错误，请提单跟踪!'




    def tearDown(self):
        driver=self.driver
        driver.close()
        self.assertEqual([],self.verificationErrors)

if __name__=='__main__':
    suite=unittest.TestSuite()
    #suite.addTest(Baidu('testBaidu'))
    suite.addTest(unittest.makeSuite(baidu.Baidu))

    #定义报告存放路劲
    filename="D:\\Git\\PyCharm\\pythonSelenium2\\report\\result.html"
    fp=file(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'百度测试报告',
        description=u'用例执行情况:'
    )
    runner.run(suite)
    #关闭报告文件
    fp.close()







