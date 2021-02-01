from selenium import webdriver
import time
import schedule
from selenium.webdriver import ActionChains
import datetime
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import sys
import os

def run():

    # 从txt文件读取LOIS 登陆信息，只需在txt文件维护登陆信息即可
    file = open(r"E:\workspaceprod\cuichuang1\Daily SBB Asynch Check\windchill.txt","r") #修改文件路径
    login = file.readlines()
    username = (login[0].strip()).replace('\n','')
    pw = (login[1].strip()).replace('\n','')
    file.close()

    # change the download path
    chromeOptions = webdriver.ChromeOptions()
    # prefs = {"download.default_directory": "E:\workspaceprod\qinn1\MTM_Report_Upgrade\init_mtm"} #修改文件路径
    # chromeOptions.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chrome_options=chromeOptions)
    driver.implicitly_wait(5)

    # ??????
    driver.get(r'http://bjplmapp.lenovo.com/Windchill/app/')

    # reload webpage(lois)
    time.sleep(3)
    pyautogui.moveTo(x=103,y=67,duration=0.5)
    time.sleep(0.5)
    pyautogui.click()

    # auto enter itcode and password to login 
    time.sleep(3)
    pyautogui.moveTo(x=463, y=182, duration=0.5)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.typewrite(username, 0.1)
    time.sleep(1)
    pyautogui.moveTo(x=463, y=249, duration=0.5)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.typewrite(pw, 0.1)
    time.sleep(1)
    pyautogui.press("enter")
    pyautogui.moveTo(x=630, y=284, duration=0.5)
    time.sleep(1)
    pyautogui.click()
    time.sleep(8)

    # pyautogui.hotkey("alt"," ")
    # time.sleep(0.5)
    # pyautogui.hotkey("n")
    

    print(driver.title)

  
    time.sleep(1)
if __name__ == '__main__':
    run()