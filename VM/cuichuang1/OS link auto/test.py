# import time
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# import os
# import openFlash
# from openFlash import openFlash
# browser = webdriver.Chrome()
# # 访问页面
# url = r'http://lois.lenovo.com/lenovo-lois-web/main/main.html'
# browser.get(url)#打开浏览器预设网址
# # 最大化
# browser.maximize_window()
# # 刷新
# browser.refresh()
import time
import pyautogui as pg

pg.FAILSAFE=False
pg.PAUSE = 1
# 获取当前屏幕像素
width,height = pg.size()
# time.sleep(2)
print (width,height)
x,y = pg.position()
print(x,y)
