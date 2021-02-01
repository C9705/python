from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os
import openFlash
from openFlash import openFlash
import pyautogui as pg

def finalAndUpload():
    import pyautogui as pg
    # os.chdir(r'C:\Users\cuichuang1\Desktop\OS link auto\\')
    # 获取查询数据
    import pandas as pd
    osData = pd.read_excel(filePath, dtype=str)
    print(osData)
    # print(str(osData.columns.values))
    osData = [i for i in list(osData) if str.find(i, 'Unnamed') < 0]
    str1 = ','.join(osData)
    print(str1)
    #browser = webdriver.Chrome()
    # 访问页面
    #url = r'http://lois.lenovo.com/lenovo-lois-web/main/main.html'
    #browser.get(url)  # 打开浏览器预设网址
    # 最大化
    #browser.maximize_window()
    # 刷新
    #browser.refresh()
    # deal flash
    #openFlash()
    #time.sleep(10)

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
    # # 获取当前屏幕像素
    # width,height = pg.size()
    # # time.sleep(2)
    # print (width,height)
    # x,y = pg.position()
    # print(x,y)
    # # 打开浏览器
    # pg.moveTo(225,765,duration=1)
    # pg.click()
    # time.sleep(0.5)
    # # 浏览器最大化
    # pg.hotkey("alt"," ")
    # time.sleep(0.5)
    # pg.hotkey("x")
    # time.sleep(0.5)
    # pg.hotkey("alt","D")
    #
    # pg.typewrite(message=Address,interval=0.2)
    # pg.press("enter")
    # print("finish")
    # time.sleep(2)
    # 点击flash
    # pg.moveTo(161,50,duration=0.2)
    # pg.click()
    # pg.moveTo(344,204,duration=0.2)
    # pg.click()
    # pg.moveTo(343,260,duration=0.2)
    # pg.click()
    # pg.moveTo(85,51,duration=0.2)
    # pg.click()
    # pg.sleep(1)

    # # SBB Management click
    # pg.moveTo(14, 400, duration=0.2)
    # pg.click()
    # # maintain SBB
    # pg.moveTo(91, 422, duration=0.2)
    # pg.click()
    # # Search CTO
    # pg.moveTo(345, 264, duration=0.2)
    #
    # pg.click()
    # # 输入CTO
    # pg.moveTo(854, 380, duration=0.2)
    # pg.click()
    # pg.typewrite(message="20UNCTO1WW",interval=0.01)
    # # pg.typewrite(message=CTOnum, interval=0.01)
    # # SBB Basic Name
    # pg.moveTo(525, 462, duration=0.2)
    # pg.click()
    # pg.typewrite(message="L1 OSL", interval=0.1)
    # # status
    # pg.moveTo(1008, 433, duration=0.2)
    # pg.click()
    # pg.moveTo(880, 512, duration=0.2)
    # pg.click()
    # # Search
    # pg.moveTo(885, 487, duration=0.2)
    # pg.click()
    # time.sleep(20)
    #
    # # Select ALL
    # pg.moveTo(325, 293, duration=0.2)
    # pg.click()
    #
    # # view links
    # pg.moveTo(521, 261, duration=0.2)
    # pg.click()
    # pg.moveTo(511, 292, duration=0.2)
    # pg.click()
    # time.sleep(5)
    #
    # pg.moveTo(277,232,duration=0.2)
    # pg.click()
    # time.sleep(1)
    # pg.moveTo(304, 211, duration=0.2)
    # pg.click()
    # time.sleep(1)
    #


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
    time.sleep(30)
    # 全选
    browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[3]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div/div[1]').click()
    time.sleep(1)
    # view link
    # browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[3]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/div[5]').click()
    # time.sleep(1)
    # loadsheet upload
    browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[3]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/div[7]/em/button').click()
    time.sleep(1)
    # Element link loadsheett_3
    browser.find_element_by_xpath('/html/body/div[13]/div[1]/div[2]/div[3]/a').click()
    time.sleep(5)
    import pyautogui as pg
    # 保护措施，防止产生异常
    pg.FAILSAFE = False
    # # 操作等待
    pg.PAUSE = 1
    # # 获取当前屏幕像素
    width, height = pg.size()
    print(width, height)
    # # 获取鼠标当前位置坐标 position()
    # # initialMouseX,initialMouseY  = pg.position()
    # # print(initialMouseX,initialMouseY)
    # #
    # # # Search
    pg.click(991,287)
    time.sleep(5)
    pg.moveTo(1014, 284, duration=1)
    pg.click()


    pg.typewrite(message=r"C:\Users\cuichuang1\Desktop\element_link_tool\dist\element_link_tool\upload_os_3.xlsx", interval=0.5)
    time.sleep(5)
    pg.moveTo(679,446)
    time.sleep(1)
    pg.click()
    time.sleep(1)
    pg.moveTo(666,446)
    time.sleep(1)
    pg.click()
    time.sleep(1)
    pg.moveTo(661,463)
    time.sleep(1)
    pg.click()
    time.sleep(2)
    pg.moveTo(988, 279)
    time.sleep(1)
    pg.click()
    time.sleep(1)
    # more
    browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[3]/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/div[2]/div[9]').click()
    # Promote
    browser.find_element_by_xpath('/html/body/div[14]/div[1]/div[2]/div[3]').click()

    # yes
    browser.find_element_by_xpath('/html/body/div[15]/div[3]/div/div[2]/em/button').click()

    browser.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div[4]/div/div[12]').click()

    browser.find_element_by_xpath('//ul/li[contains(text(),"500")]').click()

    # 全选
    browser.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div[5]/div/div[1]').click()

    browser.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div/div[1]').click()
    # li final
    browser.find_element_by_xpath('/html/body/div[6]/div/ul/li[2]').click()

    # promote final
    browser.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div[2]/div/div[1]/em/button').click()
# SBB0J17596
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

if __name__=='__main__':
    # getPath()
    finalAndUpload()

