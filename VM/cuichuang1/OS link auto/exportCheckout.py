from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os
import pyautogui
# import openFlash
# from openFlash import openFlash

def getData(filePath):
    # os.chdir(r'C:\Users\cuichuang1\Desktop\OS link auto\\')
    # 获取查询数据
    # import pandas as pd
    # osData = pd.read_excel(filePath,dtype= str)
    # print(osData)
    # # print(str(osData.columns.values))
    # osData = [i for i in list(osData) if str.find(i,'Unnamed')<0]
    # str1 = ','.join(osData)
    # print(str1)

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
    browser.get('http://lois.lenovo.com/lenovo-lois-web/main/main.html')

    # reload webpage(lois)
    time.sleep(3)
    pyautogui.moveTo(x=103, y=67, duration=0.5)
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
    pyautogui.moveTo(x=463, y=226, duration=0.5)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.typewrite(pw, 0.1)
    time.sleep(1)
    pyautogui.moveTo(x=630, y=284, duration=0.5)
    time.sleep(1)
    pyautogui.click()
    time.sleep(8)
    pyautogui.press("enter")
    print(browser.title)

    for handle in browser.window_handles:
        browser.switch_to.window(handle)
        if 'lois' in driver.title:
            break
    time.sleep(1)



    # import pyautogui
    # 声明调用的浏览器
    # browser = webdriver.Chrome()
    # 访问页面
    # url = r'http://lois.lenovo.com/lenovo-lois-web/main/main.html'
    # browser.get(url)#打开浏览器预设网址
    # 最大化
    # browser.maximize_window()
    # 刷新
    # browser.refresh()
    # 点击
    # Expand ALL
    # time.seep(60)
    # username
    # pg.moveto(583,163,duration=1)
    # pg.click()
    # pg.typewrite(message=)
    # password

    # # 调用openFlash()
    # openFlash()

    # 打开SBB Management
    sbb_maintain=browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div[3]/div/div[2]/div/table/tbody/tr[8]/td/div')
    # 双击
    action_chins=ActionChains(browser)
    action_chins.double_click(sbb_maintain).perform()
    time.sleep(1)
    # SBB Maintain
    browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div[3]/div/div[2]/div/table/tbody/tr[9]/td/div').click()
    time.sleep(1)
    # Search
    browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[3]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/div[1]/em/button/span').click()
    # 输入CTO
    browser.find_element_by_xpath('/html/body/div[11]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/input').send_keys(str1)
    # 选择状态
    browser.find_element_by_xpath('/html/body/div[11]/div[2]/div/div[1]/div[4]/div/div[2]/div[1]/input').click()
    browser.find_element_by_xpath('//ul/li[contains(text(), "Initiated")]').click()
    time.sleep(0.5)
    # 输入Basic name
    browser.find_element_by_xpath('/html/body/div[11]/div[2]/div/div[1]/div[5]/div/div[1]/div[1]/input').send_keys('L1 OSL')

    # Search
    browser.find_element_by_xpath('/html/body/div[11]/div[2]/div/div[2]/div/div[2]/em/button/span').click()
    time.sleep(30)

    browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[3]/div[2]/div[2]/div/div[1]/div[2]/div/div[3]/div/div[12]').click()
    browser.find_element_by_xpath('//ul/li[contains(text(),"500")]').click()
    time.sleep(21)
    # print('done')
    # 全选
    browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[3]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div/div[1]').click()
    # view link
    browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[3]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/div[5]').click()

    time.sleep(1)
    browser.find_element_by_xpath('//a/span[contains(text(), "View Links")]').click()
    time.sleep(5)


    #
    # import pyautogui as pg
    # # 保护措施，防止产生异常
    # pg.FAILSAFE=False
    # # # 操作等待
    # pg.PAUSE = 1
    # # # 获取当前屏幕像素
    # width,height = pg.size()
    # print(width,height)
    # pg.moveTo(325,293,duration=0.2)
    # pg.click()
    # pg.moveTo(767,264,duration=0.2)
    # pg.click()
    # pg.moveTo(789,313,duration=0.2)
    # pg.click()
    # pg.press("enter")
    # # promote
    # pg.moveTo(325,293,duration=0.2)
    # pg.click()
    # pg.moveTo(585,267,duration=0.2)
    # pg.click()
    # pg.moveTo(485,305,duration=0.2)
    # pg.click()
    # pg.moveTo(344,265,duration=0.2)
    # pg.click()
    # pg.press("enter")
    # print('DONE')
#     # # 获取鼠标当前位置坐标 position()
#     # # initialMouseX,initialMouseY  = pg.position()
#     # # print(initialMouseX,initialMouseY)
#     # #
#     # # # Search
#     time.sleep(5)
#     pg.moveTo(265,194,duration=1)
#     pg.click()
#     # # # # 文本框
#     pg.moveTo(532,422,duration=1)
#     pg.click()
#     # # # # 输入信息
#     pg.typewrite(message='4 Digital Mic',interval=0.5)
#     # # #
#     # # # # Search2
#     pg.moveTo(638,564,duration=1)
#     pg.click()
#     #
#     # # element 740 281
#     pg.moveTo(740,281,duration=1)
#     pg.dragTo(x= 292, y= 249, duration=1,button='left')
#     #
#     # # export with checkout
#     pg.moveTo(655,187,duration=1)
#     pg.click()

#     time.sleep(2)

#     browser.close()#关闭浏览器


def getPath():
    import os
    global filePath
    pathNow = os.path.dirname(__file__)
    print(pathNow)
    files = os.listdir(pathNow)
    print(files)
    for i in files:
        if str.find(i, 'osAuto.xlsm') != -1:
            filePath = pathNow +'\\' + i
            print(filePath)
            return filePath


# import pyautogui as pg
# def openFlash():
#     pass
# # 保护措施
#     pg.FAILSAFE=False
#     pg.PAUSE = 1
#     # 获取当前屏幕像素
#     width, height = pg.size()
#     time.sleep(2)
#     x,y = pg.position()
#     print(x,y)
#     # 1
#     pg.moveTo(135,46)
#     pg.click()
#     # # # 2
#     pg.moveTo(365,219)
#     pg.click()
#     # # 3
#     pg.moveTo(378,272)
#     pg.click()

if __name__ == '__main__':
    getPath()
    getData("1")


# #
#
#
# # browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[3]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div/div[1]/div/span').click()
#
#
# # [‎2020 /‎6 /‎23
# # 15: 18]  Guangsheng
# # GS5
# # Xu:
# # ac = ActionChains(driver)
# # ac.move_to_element(driver.find_element_by_xpath('//a/span[contains(text(), "Columns")]')).perform()
#
