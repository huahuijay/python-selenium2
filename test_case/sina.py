#!-*- coding:utf-8 -*-
import unittest
import time
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')
'''断言的测试应用'''
from selenium import webdriver
#鼠标事件
from selenium.webdriver.common.action_chains import ActionChains
#键盘事件
from selenium.webdriver.common.keys import  Keys
#超时等待
from selenium.webdriver.support.ui import WebDriverWait

#引用封装的类
from package import *
class Assertions(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.base_url='http://www.baidu.com'
        self.verificationErrors=[]
        self.accept_next_alert=True

    def testSina(self):
        driver=self.driver
        driver.get(self.base_url)
        common.findCss(driver,".tn-tab>i").click()

    #操作测试对象
    def testObject(self):
        driver=self.driver
        driver.get(self.base_url)
        #在新浪搜索输入框作为测试的对象
        so=common.findID(driver,'kw')
        so.clear()
        so.send_keys(u'sina测试')
        common.findID(driver,'su').submit()
        testText=common.findClassName(driver,'toindex').text
        try:
            self.assertEqual(u'百度首页',testText)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def testProperty(self):
        driver=self.driver
        driver.get(self.base_url)
        #百度搜索输入框的属性值
        attributeText=common.findID(driver,'kw').get_attribute('type')
        print attributeText
    #利用元素的属性测试百度搜索设置
    def testSoSet(self):
        driver=self.driver
        driver.get(self.base_url)
        common.findLinkText(driver,u'设置').click()
        common.findLinkText(driver,u'搜索设置').click()
        options=driver.find_elements_by_tag_name('option')
        value=u'100'
        for option in options:
            if option.get_attribute('value')==value:
                option.click()
        time.sleep(5)

    #判断是否可见
    def test_isDisplayed(self):
        driver=self.driver
        driver.get(self.base_url)
        result=common.findName(driver,'tj_trmap').is_displayed()
        try:
            self.assertEqual(True,result)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    #鼠标事件
    #已百度首页的更多产品，鼠标停留在为实例
    def testAction(self):
        driver=self.driver
        driver.get(self.base_url)
        above=common.findLinkText(driver,u'更多产品')
        ActionChains(driver).move_to_element(above).perform()
        time.sleep(5)

    def testKeys(self):
        '''键盘事件'''
        driver=self.driver
        driver.get(self.base_url)
        so=common.findID(driver,'kw')
        so.send_keys('webdriver')
        so.send_keys(Keys.CONTROL,'a')
        so.send_keys(Keys.DELETE)
        time.sleep(3)
        so.send_keys(Keys.F5)
        time.sleep(3)

    def testWait(self):
        '''设置等待时间'''
        driver=self.driver
        driver.get(self.base_url)
        so=WebDriverWait(driver, 10).until(lambda  driver  :common.findID(driver,'kw'))
        so.send_keys('webdriver')
        time.sleep(3)

    def testGroup(self):
        '''定位一组对象'''
        driver=self.driver
        #先已标记对定位到所有的元素，然后依据属性过滤出，点击勾选
        file_path=os.path.abspath("D:\\Git\\PyCharm\\Develop-Python-Selenium2\\html\\objects.html")
        driver.get(file_path)
        inputs=driver.find_elements_by_tag_name('input')
        for input in inputs:
            if input.get_attribute('type')=='checkbox':
                input.click()
        time.sleep(5)

    def testFrame(self):
        driver=self.driver
        file=os.path.abspath("D:\\Git\\PyCharm\\Develop-Python-Selenium2\\html\\frame.html")
        driver.get(file)
        #先寻找到frame1，再依次寻找frame2
        driver.switch_to_frame('f1')
        driver.switch_to_frame('f2')
        #对frame2中的属性进行操作
        common.findID(driver,'kw').send_keys('kw')
        time.sleep(4)



    def tearDown(self):
        driver=self.driver
        driver.quit()
        self.assertEqual([],self.verificationErrors)

if __name__=='__main__':
    unittest.main()




