import time
import pyautogui as pg
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import xlrd
def reardata():
    import pandas as pd
    import os
    global CTO
    # pathNow=os.path.dirname(__file__)
    # files = os.listdir(pathNow)
    # for i in files:
    #     if str.find(i,"osAuto.xlsm") != -1:
    #         filePath = pathNow +'/'+i
    # print(pathNow)
    # print(filePath)
    # CTO=pd.read_excel(r"E:/workspaceprod/cuichuang1/OS link auto/osAuto.xlsm",dtype=str)
    # CTO=[i for i in list(CTO) if str.find(i,'Unnamed')<0]
    # CTO = ','.join(CTO)
    # print(CTO)
    data = xlrd.open_workbook(r"E:/workspaceprod/cuichuang1/OS link auto/osAuto.xlsm").sheet_by_name('Sheet1')
    CTO=data.cell(0,0).value
    print(CTO)
def work(Address,CTOnum):
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

    # ??????
    browser.get(r"chrome://settings/content/flash")
    time.sleep(1)
    pg.hotkey("alt", " ")
    time.sleep(0.5)
    pg.hotkey("x")
    time.sleep(0.5)
    pg.hotkey("alt", "D")
    time.sleep(1)
    pg.moveTo(1006,310,duration=0.5)
    pg.click()



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
    time.sleep(2)


    pg.FAILSAFE=False
    pg.PAUSE = 1

    # SBB Management click
    pg.moveTo(14, 400, duration=0.2)
    pg.click()
    # maintain SBB
    pg.moveTo(91, 422, duration=0.2)
    pg.click()
    # Search CTO
    pg.moveTo(345, 264, duration=0.2)

    pg.click()
    # 输入CTO
    pg.moveTo(854, 380, duration=0.2)
    pg.click()
    #pg.typewrite(message="82ACCTO1WW",interval=0.01)
    pg.typewrite(message=CTOnum, interval=0.01)
    # SBB Basic Name
    pg.moveTo(525, 462, duration=0.2)
    pg.click()
    pg.typewrite(message="L1 OSL", interval=0.1)
    # status
    pg.moveTo(1008, 433, duration=0.2)
    pg.click()
    pg.moveTo(880, 512, duration=0.2)
    pg.click()
    # Search
    pg.moveTo(885, 487, duration=0.2)
    pg.click()
    time.sleep(60)
    # all
    pg.moveTo(320, 293, duration=0.2)
    pg.click()
    # view
    pg.moveTo(521, 261, duration=0.2)
    pg.click()
    pg.moveTo(511, 292, duration=0.2)
    pg.click()
    time.sleep(30)

    # fl
    pg.moveTo(265, 228, duration=0.2)
    pg.click()
    pg.moveTo(302, 207, duration=0.2)
    pg.click()
    time.sleep(5)










    # SBB Management click
    pg.moveTo(14,400,duration=0.2)
    pg.click()
    # maintain SBB
    pg.moveTo(91,422,duration=0.2)
    pg.click()
    #Search CTO
    pg.moveTo(345,264,duration=0.2)
    
    pg.click()
    # 输入CTO 
    pg.moveTo(854,380,duration=0.2)
    pg.click()
    
    #pg.typewrite(message="82ACCTO1WW",interval=0.01)
    pg.typewrite(message=CTOnum,interval=0.01)
    # SBB Basic Name
    pg.moveTo(525,462,duration=0.2)
    pg.click()
    pg.typewrite(message="L1 OSL",interval=0.1)
    # status
    pg.moveTo(1008,433,duration=0.2)
    pg.click()
    pg.moveTo(880,512,duration=0.2)
    pg.click()
    #Search
    pg.moveTo(885,487,duration=0.2)
    pg.click()
    time.sleep(120)

    # change sum
    pg.moveTo(628,466,duration=0.2)
    pg.click()
    #500
    pg.moveTo(594,563,duration=0.2)
    pg.click()
    time.sleep(30)

    #Select ALL
    pg.moveTo(325,293,duration=0.2)
    pg.click()

    # view links
    pg.moveTo(521,261,duration=0.2)
    pg.click()
    time.sleep(10)
    pg.moveTo(511,292,duration=0.2)
    pg.click()
    time.sleep(60)

    # flash
    # checkout
        # Search
    pg.moveTo(250,191,duration=0.2)
    pg.click()
    time.sleep(20)
    pg.moveTo(569,422,duration=0.2)
    pg.click()
    time.sleep(20)
    pg.typewrite(message='4 Digital Mic',interval=0.2)
    time.sleep(2)
    pg.moveTo(630,560,duration=0.2)
    pg.click()
    time.sleep(1)

    # Drag
    pg.moveTo(740,281,duration=0.2)
    pg.dragTo(x= 292, y= 249, duration=5,button='left')

    # export with checkout
    pg.moveTo(655,187,duration=1)
    pg.click()
    time.sleep(10)
    
    # close chrome
    pg.moveTo(1343,13,duration=1)
    pg.click()

if __name__ == '__main__':
    reardata()
    work(r'http://lois.lenovo.com/lenovo-lois-web/main/main.html',CTO)
    print("CHECK.PY DONE")
    # x,y = pg.position()
    # print(width,height)