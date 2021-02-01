import time
import pyautogui as pg
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import xlrd

def reardata():
    import pandas as pd
    import os
    global CTO
    data = xlrd.open_workbook(r"E:/workspaceprod/cuichuang1/OS link auto/osAuto.xlsm").sheet_by_name('Sheet1')
    CTO=data.cell(0,0).value
    print(CTO)

def work(Address,CTOnum,count,basicName):
    # login
    # 从txt文件读取LOIS 登陆信息，只需在txt文件维护登陆信息即可
    file = open(r"E:\workspaceprod\cuichuang1\Daily SBB Asynch Check\lois-login-username-pw.txt", "r")  # 修改文件路径
    login = file.readlines()
    username = (login[0].strip()).replace('\n', '')
    pw = (login[1].strip()).replace('\n', '')
    file.close()

    # change the download path
    chromeOptions = webdriver.ChromeOptions()
    # prefs = {"download.default_directory": "E:\workspaceprod\qinn1\MTM_Report_Upgrade\init_mtm"} #修改文件路径
    # chromeOptions.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(chrome_options=chromeOptions)
    browser.implicitly_wait(5)

 


    time.sleep(1)
    browser.get(r'http://lois.lenovo.com/lenovo-lois-web/main/main.html')
    # reload webpage(lois)
    time.sleep(3)
    pg.moveTo(x=103, y=67, duration=0.5)
    time.sleep(0.5)
    pg.click()

    # auto enter itcode and password to login
    time.sleep(3)
    pg.moveTo(x=463, y=182, duration=0.5)
    time.sleep(1)
    pg.click()
    time.sleep(1)

    # 浏览器最大化
    pg.hotkey("alt"," ")
    time.sleep(0.5)
    pg.hotkey("x")
    time.sleep(0.5)
    pg.hotkey("alt","D")
    time.sleep(1)
    pg.typewrite(username, 0.1)
    time.sleep(1)
    pg.moveTo(x=591, y=211, duration=0.5)
    time.sleep(1)
    pg.click()
    time.sleep(1)
    pg.typewrite(pw, 0.1)
    # time.sleep(1)
    pg.moveTo(x=775, y=264, duration=0.5)
    time.sleep(1)
    pg.click()
    time.sleep(1)
    pg.press("enter")
    print(browser.title)
    for handle in browser.window_handles:
        browser.switch_to.window(handle)
        if 'lois' in browser.title:
            break
    browser.refresh()
    time.sleep(1)
    # SBB Management
    SBB=browser.find_element_by_xpath("//*[text()='SBB Management']")
    ActionChains(browser).double_click(SBB).perform()
    time.sleep(0.5)
    #Maintain SBB
    browser.find_element_by_xpath("//*[text()='Maintain SBB']").click()
    time.sleep(0.5)
    #Search
    browser.find_element_by_xpath("//*[text()='Search']").click()
    time.sleep(0.5)
    # CTO NUm
    CTONum=browser.find_element_by_xpath('/html/body/div[11]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/input')
    browser.execute_script("arguments[0].value='"+CTO+"'",CTONum)
     # SBB Basic name
    Basic=browser.find_element_by_xpath('/html/body/div[11]/div[2]/div/div[1]/div[5]/div/div[1]/div[1]/input')
    browser.execute_script("arguments[0].value='"+basicName+"'",Basic)
    # status
    status1=browser.find_element_by_xpath('/html/body/div[11]/div[2]/div/div[1]/div[4]/div/div[2]/div[1]/input')
    browser.execute_script("arguments[0].value='Initiated'",status1)
    # Search2
    browser.find_element_by_xpath('/html/body/div[11]/div[2]/div/div[2]/div/div[2]').click()
    time.sleep(60)
    # more 500
    browser.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[3]/div[2]/div[2]/div/div[1]/div[2]/div/div[3]/div/div[12]/div[1]/div/div[1]").click()
    time.sleep(1)
    browser.find_element_by_xpath("//*[text()='50']").click()
    time.sleep(60)
    #select all
    browser.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[3]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div/div[1]/div/span").click()
    time.sleep(0.5)
    #view links
    browser.find_element_by_xpath("//*[text()='View Links']").click()
    time.sleep(0.5)
    browser.find_element_by_xpath("/html/body/div[13]/div[1]/div[2]/div[2]/a/span").click()
    time.sleep(5)
    # Search element
    pg.moveTo(223,150,duration=0.5)
    pg.click()
    # element
    pg.moveTo(525,299,duration=0.5)
    pg.click()    
    time.sleep(1)
    pg.typewrite(message='free-dos',interval=0.5)
    pg.moveTo(998,489,duration=0.5)
    pg.click()
    time.sleep(2)
    # search result
    pg.moveTo(385,320,duration=0.5)
    pg.click()
    time.sleep(0.5)
    # confirm
    pg.moveTo(878,576,duration=0.5)
    pg.click()
    print('done')
    # checkout report
    pg.moveTo(590,149,duration=0.5)
    pg.click()
    # show=browser.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[3]/div[2]/div[2]/div/div[1]/div[2]/div/div[3]/div/div[12]/div[1]/input")
    # browser.execute_script("arguments[0].value='500'",show)
    time.sleep(60)
    browser.quit()
   
if __name__ == "__main__":
    reardata()
    work(r'http://lois.lenovo.com/lenovo-lois-web/main/main.html',CTO,50,'L1 OSL')
    pass