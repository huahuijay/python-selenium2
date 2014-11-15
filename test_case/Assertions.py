#!-*- coding:utf-8 -*-
import unittest
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
'''断言的测试应用'''
from selenium import webdriver
class Assertions(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.base_url='http://www.baidu.com'
        #脚本运行时，错误的信息将打印到这个列表中
        self.verificationErrors=[]
        #是否接受下一个A警告
        self.accept_next_alert=True

    def testAssertion(self):
        '''断言的测试'''
        driver=self.driver
        driver.get(self.base_url+'/')
        #断言来判断title是否正确
        try:
            self.assertEqual(u'百度一下，你就知道',driver.title)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    '''测试错误的截图'''
    def testImage(self):
        '''错误截图的获取'''
        driver=self.driver
        driver.get('http://www.baidu.com')
        try:
            driver.find_element_by_id('kw1ffg').send_keys('webdriver')
        except:
            driver.get_screenshot_as_file('D:/Git/PyCharm/pythonSelenium2/image/error_png.png')


    def tearDown(self):
        driver=self.driver
        driver.close()
        self.assertEqual([],self.verificationErrors)

if __name__=='__main__':
    #创建测试容器
    suite=unittest.TestSuite()
    #添加测试用例
    suite.addTest(Assertions('testAssertion'))
    #suite.addTest(Assertions('testImage'))
    #unittest.makeSuite(Assertions,'test_case')
    #执行测试用例
    runner=unittest.TextTestRunner()
    #执行用例
    runner.run(suite)




