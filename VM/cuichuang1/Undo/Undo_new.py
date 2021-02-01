from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys  
import time
import pyautogui as pg
import os
import ctypes
import xlwt
import traceback
def undoSBB():
    file = open(r"C:\Users\cuichuang1\Desktop\VM\cuichuang1\Daily SBB Asynch Check\lois-login-username-pw.txt", "r")  # 修改文件路径
    login = file.readlines()
    username = (login[0].strip()).replace('\n', '')
    pw = (login[1].strip()).replace('\n', '')
    file.close()
    # chrome_driver = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"  #chromedriver的文件位置
    # browser=webdriver.Chrome(executable_path = chrome_driver)
    browser=webdriver.Chrome()
    browser.get('http://lois.lenovo.com/lenovo-lois-web/main/main.html')
    browser.maximize_window()
    browser.refresh()
    time.sleep(1)
    # login
    pg.moveTo(x=463, y=182, duration=0.5)
    time.sleep(1)
    pg.click()
    time.sleep(1)
    # 浏览器最大化
    pg.hotkey("alt", " ")
    time.sleep(0.5)
    pg.hotkey("x")
    time.sleep(0.5)
    pg.hotkey("alt", "D")
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

    # Report
    browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div[3]/div/div[2]/div/table/tbody/tr[14]/td/div/img[1]').click()
    time.sleep(1)
    pg.moveTo(295,712,duration=0.5)
    i=0
    while i<20:
        i+=1
        pg.click()
    # undo check report
    browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div[3]/div/div[2]/div/table/tbody/tr[30]/td/div').click()
    time.sleep(1)
    # Generate
    pg.moveTo(1302,515,duration=0.5)
    pg.click()
    time.sleep(5)
    browser.quit()

def GetSBB(path):
    list=os.listdir(path)
    for i in range(len(list)):
        if(list[i].find("Undo")!=-1):
            file=list[i]
            break
    SBBData=pd.read_excel(path+file,sheet_name="SBB")
    # print(SBBData['SBB Number'][0])
    # print(len(SBBData['SBB Number']))
    print(SBBData)
    str=""
    for k in range(len(SBBData['SBB Number'])):
        if(k!=(len(SBBData['SBB Number'])-1)):
            str=str+SBBData['SBB Number'][k]+","
        else:
            str=str+SBBData['SBB Number'][k]   
    print(str)
    if len(str)<=1:
        print("SBB is none x")
        return
   # LOGIN
    file = open(r"C:\Users\cuichuang1\Desktop\VM\cuichuang1\Daily SBB Asynch Check\lois-login-username-pw.txt", "r")  # 修改文件路径
    login = file.readlines()
    username = (login[0].strip()).replace('\n', '')
    pw = (login[1].strip()).replace('\n', '')
    file.close()
    chrome_driver = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"  #chromedriver的文件位置
    browser=webdriver.Chrome(executable_path = chrome_driver)
    browser.get('http://lois.lenovo.com/lenovo-lois-web/main/main.html')
    browser.maximize_window()
    browser.refresh()
    time.sleep(1)
    # login
    pg.moveTo(x=463, y=182, duration=0.5)
    time.sleep(1)
    pg.click()
    time.sleep(1)
    # 浏览器最大化
    pg.hotkey("alt", " ")
    time.sleep(0.5)
    pg.hotkey("x")
    time.sleep(0.5)
    pg.hotkey("alt", "D")
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

    # SBBMaintain
    browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div[3]/div/div[2]/div/table/tbody/tr[8]/td/div/img[1]').click()
    time.sleep(0.5) 
    # Maintain SBB
    browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div[3]/div/div[2]/div/table/tbody/tr[9]/td/div').click()
    time.sleep(0.5)
    #Search() 
    browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[3]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/div[1]/em/button').click()
    browser.find_element_by_xpath('/html/body/div[11]/div[2]/div/div[1]/div[3]/div/div[1]/div[1]/input').send_keys(str)
    browser.find_element_by_xpath('/html/body/div[11]/div[2]/div/div[2]/div/div[2]/em/button/span').click()
    time.sleep(1)
    # sum
    browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[3]/div[2]/div[2]/div/div[1]/div[2]/div/div[3]/div/div[12]/div[1]/div/div[1]').click()
    #    500 
    browser.find_element_by_xpath('//ul/li[contains(text(),"500")]').click()
    time.sleep(2)
    # 全选
    browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[3]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div/div[1]/div/span').click()
    # undo
    browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[3]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/div[11]/em/button/span/b').click()
    time.sleep(5)
    browser.quit()
# login()

# GETMTM：整理MTM，上传undo
def GetMTM(path):
    # pd.set_option('display.max_columns',None)
    # pd.set_option('display.width',None)
    # pd.set_option('display.max_rows',None)
    list=os.listdir(path)
    for i in range(len(list)):
        if (list[i].find('Undo')!=-1):
            file=list[i]
            break
    SBBData=pd.read_excel(path+file,sheet_name="Offering")
    # print(SBBData['SBB Number'][0])
    # print(len(SBBData['SBB Number']))
    print(len(SBBData))

    str=""
    str=SBBData.loc[SBBData['Offering Type']=='MTM']
    # 第一种方法
    # print(len(str))
    str['boo']=str.loc[:,['Check Out By']].isin(['litian4','libb4','wansq1','houce1','xugs5','luoli1','mayue7','zhangpeng11','baiye2','hanzn1','songzy7','lijj74','qinn1','zhangeh1','gaoyang27','guorp2','cuichuang1','fengsy5','jiayf5'])
    str=str.loc[str['boo']==True]
    str.reset_index(drop=True,inplace=True)
    # ['litian4','libb4','wansq1','houce1','xugs5','luoli1','mayue7','zhangpeng11','baiye2','hanzn1','songzy7','lijj74','qinn1','zhangeh1','gaoyang27','guorp2','cuichuang1','fengsy5','jiayf5']
    print(str['Offering Pn'])
    if len(str['Offering Pn'])<=0:
        print('MTM x')
        return
    # 第二种方法
    # print(len(str))
    # str=str.loc[:4999,['Offering Pn']]
    # print(len(str))
    # print(str)

    # save
    # 因为需要存储成xls，使用了xlwt
    # 1.创建一个工作薄
    book=xlwt.Workbook(encoding='utf-8',style_compression=0)
    # 2.添加一个sheet
    sheet=book.add_sheet('sheet1',cell_overwrite_ok=True)
    # 写入数据
    # sheet.write(0,0,"Offering Pn")
    for i in range(len(str)):
        # print(SBBData["Characteristic"][i])
        sheet.write(i,0,str['Offering Pn'][i])
        # sheet.write(i+1,1,SBBData["Value"][i])
    # 保存
    book.save(path+"MTM.xls")

    # 浏览器操作

    # login
    file = open(r"C:\Users\cuichuang1\Desktop\VM\cuichuang1\Daily SBB Asynch Check\lois-login-username-pw.txt", "r")  # 修改文件路径
    login = file.readlines()
    username = (login[0].strip()).replace('\n', '')
    pw = (login[1].strip()).replace('\n', '')
    file.close()
    chrome_driver = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"  #chromedriver的文件位置
    browser=webdriver.Chrome(executable_path = chrome_driver)
    browser.get('http://lois.lenovo.com/lenovo-lois-web/main/main.html')
    browser.maximize_window()
    browser.refresh()
    time.sleep(1)
    # login
    pg.moveTo(x=463, y=182, duration=0.5)
    time.sleep(1)
    pg.click()
    time.sleep(1)
    # 浏览器最大化
    pg.hotkey("alt", " ")
    time.sleep(0.5)
    pg.hotkey("x")
    time.sleep(0.5)
    pg.hotkey("alt", "D")
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

    # MTM Management
    browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div[3]/div/div[2]/div/table/tbody/tr[3]/td/div/img[1]').click()
    time.sleep(1)
    #MTM Management
    browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div[3]/div/div[2]/div/table/tbody/tr[4]/td/div').click()
    time.sleep(1)
    # Search
    browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[3]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div/div[1]/em/button').click()
    time.sleep(1)
    # browser
    browser.find_element_by_xpath('/html/body/div[11]/div[2]/div/div[1]/div[13]/div/div[1]/div[1]/div').click()
    time.sleep(1)
    # upload file
    uploadfile('UploadResult2.exe')
    time.sleep(2)
    # Search
    browser.find_element_by_xpath('/html/body/div[11]/div[2]/div/div[2]/div/div[2]/em/button/span').click()
    time.sleep(60)
    # 500
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[3]/div[2]/div[2]/div/div[1]/div[2]/div/div[3]/div/div[12]/div[1]/div/div[1]').click()
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[14]/div/ul/li[5]').click()
    time.sleep(60)
    # select all
    browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[3]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div/div[1]/div/span').click()
    time.sleep(1)
    # Undo
    browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[3]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div/div[11]/em/button/span').click()
    time.sleep(60)
    browser.quit()
# 处理CV
def CV(path):
   
    list=os.listdir(path)
    for i in range(len(list)):
        if (list[i].find('Undo')!=-1):
            file=list[i]
            break
    SBBData=pd.read_excel(path+file,sheet_name="CV")
    # print(SBBData['SBB Number'][0])
    # print(len(SBBData['SBB Number']))
    print(len(SBBData))
    if len(SBBData)<=0:
        print("CV x")
        return
    str=""
    SBBData.drop('Check Out By',axis=1,inplace=True)
    # 因为需要存储成xls，使用了xlwt
    # 1.创建一个工作薄
    book=xlwt.Workbook(encoding='utf-8',style_compression=0)
    # 2.添加一个sheet
    sheet=book.add_sheet('sheet1',cell_overwrite_ok=True)
    # 写入数据
    sheet.write(0,0,"Characteristic")
    sheet.write(0,1,"Value")
    for i in range(len(SBBData["Characteristic"])):
        # print(SBBData["Characteristic"][i])
        sheet.write(i+1,0,SBBData["Characteristic"][i])
        sheet.write(i+1,1,SBBData["Value"][i])
    # 保存
    book.save(path+"CV.xls")
    # 打开lois

    file = open(r"C:\Users\cuichuang1\Desktop\VM\cuichuang1\Daily SBB Asynch Check\lois-login-username-pw.txt", "r")  # 修改文件路径
    login = file.readlines()
    username = (login[0].strip()).replace('\n', '')
    pw = (login[1].strip()).replace('\n', '')
    file.close()
    chrome_driver = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"  #chromedriver的文件位置
    
    browser=webdriver.Chrome(executable_path = chrome_driver)
    browser.get('http://lois.lenovo.com/lenovo-lois-web/main/main.html')
    browser.maximize_window()
    browser.refresh()
    time.sleep(1)
    # login
    pg.moveTo(x=463, y=182, duration=0.5)
    time.sleep(1)
    pg.click()
    time.sleep(1)
    # 浏览器最大化
    pg.hotkey("alt", " ")
    time.sleep(0.5)
    pg.hotkey("x")
    time.sleep(0.5)
    pg.hotkey("alt", "D")
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

    # CTO Management
    browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div[3]/div/div[2]/div/table/tbody/tr[2]/td/div/img[1]').click()
    time.sleep(1)
    # maintain CV
    browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div[3]/div/div[2]/div/table/tbody/tr[5]/td/div').click()
    time.sleep(2)
    # Search
    pg.moveTo(1325,240,duration=1)
    pg.click()
    time.sleep(1)
    # Browser
    pg.moveTo(907,520,duration=1)
    pg.click()
    time.sleep(2)
    # upload
    uploadfile('UploadResult.exe')
     # Search
    pg.moveTo(950,552,duration=1)
    pg.click()
    time.sleep(60)
    # 500
    pg.moveTo(627,714,duration=1)
    pg.click()
    time.sleep(0.5)
    pg.moveTo(604,695,duration=1)
    pg.click()
    time.sleep(60)
    # 全选
    pg.moveTo(325,270,duration=1)
    pg.click()
    time.sleep(1)
    # undo
    # 540229
    pg.moveTo(544,239,duration=1)
    pg.click()

    time.sleep(60)
    browser.quit()
   
def deleteFile(path):
    # 删除文件
    pass
    list=os.listdir(path)
    for i in range(len(list)):
        if (list[i].find('Undo')!=-1):
            file=list[i]
            break
    os.remove(path+file)

# GetSBB(r"C:\Users\cuichuang1\Downloads\\")
# GetMTM(r"C:\Users\cuichuang1\Downloads\\")

def uploadfile(file):
    import os 
    main = r"C:\Users\cuichuang1\Desktop\VM\cuichuang1\Undo\Auto\\"+file
    r_v = os.system(main)
    print (r_v)
    print(main)


if __name__ == "__main__":
    import  sys
    f=open(r'C:\Users\cuichuang1\Desktop\VM\cuichuang1\Undo\undo.txt',"r+")
    f.truncate()
    f.close()
    class Logger(object):
        def __init__(self, fileN="Default.log"):
            self.terminal = sys.stdout
            self.log = open(fileN, "a+")

        def write(self, message):
            self.terminal.write(message)
            self.log.write(message)

        def flush(self):
            pass


    sys.stdout = Logger(r"C:\Users\cuichuang1\Desktop\VM\cuichuang1\Undo\undo.txt")  # 这里我将Log输出到D盘
    sys.stderr = Logger(r"C:\Users\cuichuang1\Desktop\VM\cuichuang1\Undo\undo.txt")
    # //////////////////////////////////////
    # uploadfile('UploadResult2.exe')
    print(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())))
    log=[]
    try:
        undoSBB()
    # # undo SBB
    # guoyn    \RachelLi
        GetSBB("C:\\Users\\guoyn\\Downloads\\")
        time.sleep(5)
    # # undo CV
        CV("C:\\Users\\guoyn\\Downloads\\")
        time.sleep(5)
        GetMTM("C:\\Users\\guoyn\\Downloads\\")
    # # delete undo file
        deleteFile("C:\\Users\\guoyn\\Downloads\\")
        print(log)
    except Exception:
            log.append(traceback.print_exc())
            print(log)
    print('done')
    #.............................
