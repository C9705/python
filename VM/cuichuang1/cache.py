from selenium.webdriver.common.by import By
import time
from selenium import webdriver
import pyautogui as pg
from selenium.webdriver.common.action_chains import ActionChains
import os
import traceback
import logging

logging.basicConfig(filename='log.log')
def cache():
    browser = webdriver.Chrome()
    browser.get(r"chrome://settings/privacy/")
    browser.maximize_window()
    time.sleep(2)
    pg.moveTo(688,264,duration=1)
    pg.click()
    time.sleep(1)
    pg.moveTo(876,624,duration=1)
    pg.click()
    time.sleep(1) 
   
    browser.close()
if __name__ == "__main__":
    try:
        cache()
    except:
        s = time.strftime("%d/%m/%Y %H:%M:%S")+traceback.format_exc()
        logging.error(s)
        f = open(r"E:\workspaceprod\cuichuang1\OS link auto\text.txt", 'w+')
        f.writelines(s)
        f.close()
    # repr(s)
