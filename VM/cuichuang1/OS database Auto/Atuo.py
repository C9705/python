import time
import pyautogui as pg
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import py7zr
import numpy as np
import pandas as pd
import os
import zipfile
def auto(uname,password):
    # chrome_driver = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"  #chromedriver的文件位置
    
    # browser=webdriver.Chrome(executable_path = chrome_driver)
    browser=webdriver.Chrome()
    # browser.get(r"https://km.xpaas.lenovo.com/display/WCWMT/OS+Database+File+-+Houce")
    browser.get(r'https://km.xpaas.lenovo.com/pages/viewpageattachments.action?pageId=64751970')
    browser.maximize_window()
    browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/form/fieldset/div[1]/input').send_keys(uname)
    browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/form/fieldset/div[2]/input').send_keys(password)
    # browser.sendkeys('1')
    browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/form/fieldset/div[4]/input').click()

    # 回车  
    # send_keys(Keys.ENTER)
    # 下载全部附件
    time.sleep(3)
    # browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[3]/div[3]/div/div[1]/a').click()
    browser.find_element_by_xpath("//*[text()='下载全部']").click()
    time.sleep(5)
    browser.quit()


  



def dealFile():
    Path=r"E:\workspaceprod\Common\oslink_database\\"
    x=os.listdir(r'E:\workspaceprod\cuichuang1\OS database Auto\data\\')
    database_os=''
    upload_os=''
    for f in x:
        if 'database_' in f:
            database_os=f
        if 'upload_' in f:
            upload_os=f
    print(database_os)
    print(upload_os)
    os.remove(r"E:\workspaceprod\Common\oslink_database\upload_os.xlsx")
    os.remove(r"E:\workspaceprod\Common\oslink_database\database_os.xlsx")
    os.rename(r'E:\workspaceprod\cuichuang1\OS database Auto\data\\'+database_os,r"E:\workspaceprod\Common\oslink_database\database_os.xlsx")
    os.rename(r'E:\workspaceprod\cuichuang1\OS database Auto\data\\' + upload_os, r"E:\workspaceprod\Common\oslink_database\upload_os.xlsx")
    # os.remove(r'E:\workspaceprod\cuichuang1\OS database Auto\data\\'+database_os)
    # os.remove(r'E:\workspaceprod\cuichuang1\OS database Auto\data\\' + upload_os)
    # os.replace(Path+'upload_os.xlsx',Path+upload_os)
    # os.replace(Path + 'database_os.xlsx', Path + database_os)
    # os.replace(path+'upload_os.xlsx')
    # # 重命名
    # if os.path.exists(Path+'upload_os.xlsx'):
    #     os.replace(Path+'upload_os.xlsx',Path+upload_os)
    # # else:
    # #     os.rename(Path+upload_os,Path+'upload_os.xlsx')
    #
    # if os.path.exists(Path+'database_os.xlsx'):
    #     os.replace(Path+'database_os.xlsx',Path+database_os)
    # else:
    #     os.rename(Path+database_os,Path+'database_os.xlsx')
 

def file1(Path,Path2):
    # Path=r'C:\Users\guoyn\Downloads\\'
    arr=os.listdir(Path)
# list=os.listdir(Path)
    arr=list(filter(lambda x:x.find('download')!=-1,arr))
    print(len(arr))
    # Path2=r'C:\Users\cuichuang1\Desktop\os database update\\'
    if len(arr)!=0:
        Unzip(arr[0],Path,Path2)
        os.remove(Path+arr[0])  
        arr=os.listdir(Path2)
        arr=sorted(arr,reverse=True)
        print(arr[0])
        Un7z(arr[0],Path,Path2)
        for i in arr:
            os.remove(Path2+i)
        print('done')
        
import zipfile
def Unzip(zip,Path,Path2):
    #解压文件
    extracting = zipfile.ZipFile(Path+zip)
    #解压出文件，存放路径
    extracting.extractall(Path2) 
    extracting.close()

def Un7z(x,Path,Path2):
    a = py7zr.SevenZipFile(Path2+x,'r')
    a.extractall(path=r'E:\workspaceprod\cuichuang1\OS database Auto\data\\')
    a.close()

def getUnPs():
    global uname,password
    # Path=r"E:\workspaceprod\cuichuang1\OS database Auto\Xpaas-una-pas.txt"
    # with open(r"E:\workspaceprod\cuichuang1\OS database Auto\Xpaas-una-pas.txt",'r') as r:
    with open(r"C:\Users\cuichuang1\Desktop\VM\cuichuang1\OS database Auto\Xpaas-una-pas.txt",'r') as r:
        data=r.read().splitlines()
        uname=data[0]
        password=data[1]
        print(uname, password)
        return uname,password

        # print(data[0].split("\\")[0])


        
if __name__ == "__main__":
    import  sys
    # f=open(r'E:\workspaceprod\cuichuang1\OS database Auto\log.txt',"r+")
    f=open(r'C:\Users\cuichuang1\Desktop\VM\cuichuang1\OS database Auto\log.txt',"r+")
    f.truncate()
    f.close()
    class Logger(object):
        def __init__(self, fileN="Default.log"):
            self.terminal = sys.stdout
            self.log = open(fileN, "a")

        def write(self, message):
            self.terminal.write(message)
            self.log.write(message)

        def flush(self):
            pass
    

    # sys.stdout = Logger(r"E:\workspaceprod\cuichuang1\OS database Auto\log.txt")  # 这里我将Log输出到D盘
    sys.stdout = Logger(r"C:\Users\cuichuang1\Desktop\VM\cuichuang1\OS database Auto\log.txt")

    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    getUnPs()
    auto(uname,password)
    time.sleep(5)
    #"C:\Users\guoyn\Downloads\chromedriver_win32"
    # \RachelLi
    file1(r'C:\Users\guoyn\Downloads\\',r'E:\workspaceprod\cuichuang1\OS database Auto\data\\')
    dealFile()