#coding:gbk

from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import datetime
import os
import pyautogui


def run():
    
    # read login in details from file
    file = open(r"E:\workspaceprod\qinn1\SPB\app\lois-login-username-pw.txt","r")
    login = file.readlines()
    username = (login[0].strip()).replace('\n','')
    pw = (login[1].strip()).replace('\n','')
    file.close()

    #driver = webdriver.Chrome(executable_path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    #driver.implicitly_wait(5)

    # change the download path
    
    chromeOptions = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": "E:\\workspaceprod\\qinn1\\SPB\\download"}
    
    chromeOptions.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chrome_options=chromeOptions)
    driver.implicitly_wait(5)
    
    #clear Chrome cache
    driver.get('chrome://settings/clearBrowserData')
    time.sleep(3)
    pyautogui.moveTo(x=561,y=292,duration=0.5)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(x=433,y=383,duration=0.5)
    time.sleep(0.5)
    pyautogui.click()
    pyautogui.moveTo(x=722,y=626,duration=0.5)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(2)
    
    #enable Chrome Flash player
    driver.get('chrome://settings/content/flash')
    time.sleep(3)
    pyautogui.moveTo(x=452,y=332,duration=0.5)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(5)

    #最大等待时间
    
    driver.get('http://lois.lenovo.com/lenovo-lois-web/main/main.html')
    # time.sleep(5)

    # reload webpage(lois)
    time.sleep(3)
    pyautogui.moveTo(x=103,y=67,duration=0.5)
    time.sleep(0.5)
    pyautogui.click()

    #auto enter itcode & password
    time.sleep(3)
    pyautogui.moveTo(x=471,y=185,duration=0.5)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(1)
    pyautogui.typewrite(username,0.1)
    time.sleep(1)
    pyautogui.moveTo(x=453,y=226,duration=0.5)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.typewrite(pw,0.1)
    time.sleep(1)
    pyautogui.moveTo(x=631,y=286,duration=0.5)
    time.sleep(1)
    pyautogui.click()
    time.sleep(8)

    print(driver.title)

    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        if 'lois' in driver.title:
            break

    #click "mtm management"
    time.sleep(1)
    MTM_Management=driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div[3]/div/div[2]/div/table/tbody/tr[3]/td/div')
    action_chains = ActionChains(driver)
    action_chains.double_click(MTM_Management).perform()

    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div[3]/div/div[2]/div/table/tbody/tr[4]/td/div").click()

    #click "Loadsheet upload"
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[3]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div/div[7]').click()

    #click "WC MMR loadsheet"
    driver.find_element_by_xpath('/html/body/div[10]/div[1]/div[2]/div[3]').click()

    #click "adobe flash" icon
    time.sleep(2)
    pyautogui.moveTo(x=217,y=335,duration=0.5)
    time.sleep(0.5)
    pyautogui.click()

    #click "allow" in pop-up windown for adobe flash
    time.sleep(2)
    pyautogui.moveTo(x=323,y=229,duration=0.5)
    time.sleep(0.5)
    pyautogui.click()


    #upload formally starts
    #click "mtm management"
    time.sleep(3)
    MTM_Management=driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div[3]/div/div[2]/div/table/tbody/tr[3]/td/div')
    action_chains = ActionChains(driver)
    action_chains.double_click(MTM_Management).perform()

    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div[3]/div/div[2]/div/table/tbody/tr[4]/td/div").click()

    #click "Loadsheet upload"
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[3]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div/div[7]').click()

    #click "WC MMR loadsheet"
    driver.find_element_by_xpath('/html/body/div[10]/div[1]/div[2]/div[3]').click()

    #click "browse" in "WC MMR loadsheet"
    #wait longer time since flash player may be out of date and need to download a new one
    time.sleep(90)
    pyautogui.moveTo(x=856,y=282,duration=0.5)
    time.sleep(0.5)
    pyautogui.click()

    #execute UploadFile.exe
    time.sleep(1)
    os.system("E:\\workspaceprod\\qinn1\\SPB\\app\\UploadResult.exe")
    
    #click "yes" to confirm upload
    time.sleep(10)
    pyautogui.moveTo(x=498,y=457,duration=0.5)
    time.sleep(0.5)
    pyautogui.click()

    #click "confirm" to proceed
    time.sleep(10)
    pyautogui.moveTo(x=856,y=282,duration=0.5)
    time.sleep(0.5)
    pyautogui.click()

    #click "yes" in "upload successfully"
    time.sleep(10)
    pyautogui.moveTo(x=550,y=440,duration=0.5)
    time.sleep(0.5)
    pyautogui.click()

    time.sleep(20)

    
    mainWindow = driver.current_window_handle
    #这个是当前窗口的句柄
    #driver.switch_to.window(mainWindow)
    print (mainWindow)


    #settimeout(fonction(){debugger},5000s)
    driver.quit()

run() 


#import win32com.client as win32

#excel = win32.gencache.EnsureDispatch('Excel.Application')
#wb = excel.Workbooks.Open('d:\\tools\\spb\\app\\Lookup.xlsm')
#excel.Visible = True

#查找文件
#path="d:\\tools\\spb\\download"
#os.listdir()方法，列出来所有文件
#返回path指定的文件夹包含的文件或文件夹的名字的列表
#files=os.listdir(path)

#主逻辑
#对于批量的操作，使用FOR循环
#for f in files:
    #调试代码的方法：关键地方打上print语句，判断这一步是不是执行成功
#    print(f)

#exce1 = win32.gencache.EnsureDispatch('Excel.Application')
#wb = exce1.Workbooks.Open('d:\\tools\\spb\\download\\'+ f)
#exce1.Visible = True

