# -*-coding: utf-8 -*-
# @Time: 2020/7/8 10:54
# @aUTHOR : xiaopang
# @File : .py
'''调用百度'''
from selenium import webdriver
import time
browser = webdriver.Chrome(r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
browser.get('https://www.baidu.com/')
browser.maximize_window()
time.sleep(3)
browser.close()






