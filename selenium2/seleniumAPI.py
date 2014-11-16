#!-*- coding:utf-8 -*-
'''
Created on 2014-11-16
@description:selenium2 webdriver API code
@author: Administrator
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from selenium2 import webdriver
from selenium2.webdriver.common.keys import Keys
from selenium2.webdriver.support.ui import Select
from selenium2.common.exceptions import NoSuchElementException
from selenium2.webdriver.common.by import By
import unittest,time,re,os,time

#导入公共的类
from package import common

class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.base_url=''
        self.verificationErrors=[]
        self.accept_next_alert=True


    def tearDown(self):
        driver=self.driver
        driver.close()
        self.assertEqual([],self.verificationErrors)

if __name__=='__main__':
    unittest.main()






