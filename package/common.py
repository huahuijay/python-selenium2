#!-*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

'''
1、webdriver的二次封装
2、采用page object设计模式,简化代码
'''

from selenium import webdriver



'''定位单个元素封装'''
def findID(driver,id):
    f=driver.find_element_by_id(id)
    return f

def findName(driver,name):
    f=driver.find_element_by_name(name)
    return f

def findClassName(driver,name):
    f=driver.find_element_by_class_name(name)
    return f

def findTagName(driver,name):
    f=driver.find_element_by_tag_name(name)
    return f

def findLinkText(driver,text):
    f=driver.find_element_by_link_text(text)
    return f

def findPLinkText(driver,text):
    f=driver.find_element_by_partial_link_text(text)
    return f

def findXpath(driver,xpath):
    f=driver.find_element_by_xpath(xpath)
    return f

def findCss(driver,css):
    f=driver.find_element_by_css_selector(css)
    return f

'''定位一组元素封装'''
def findsID(driver,id):
    f=driver.find_elements_by_id(id)
    return f

def findsName(driver,name):
    f=driver.find_elements_by_name(name)
    return f

def findsClassName(driver,name):
    f=driver.find_elements_by_class_name(name)
    return f

def findTagName(driver,name):
    f=driver.find_element_by_tag_name(name)
    return f

def findsLinkText(driver,text):
    f=driver.find_elements_by_link_text(text)
    return f

def findsPLinkText(driver,text):
    f=driver.find_elements_by_partial_link_text(text)
    return f

def findsXpath(driver,xpath):
    f=driver.find_elements_by_xpath(xpath)
    return f

def findsCss(driver,css):
    f=driver.find_elements_by_css_selector(css)
    return f
