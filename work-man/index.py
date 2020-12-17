import os
import time
import pandas as pd

def work():
    pd.set_option('display.max_rows',None)
    pd.set_option('display.max_columns',None)
    pd.set_option('display.width',None)
    # 当前路径下文件
    print(os.listdir())
    #当前文件路径
    print(os.path.dirname(__file__))

    print(os.listdir(os.path.dirname(__file__)+"\\Source"))
    print(os.listdir('.\\Source'))
    sourceData=pd.read_excel(os.listdir('.\\Source')[0],sheet_name="总",dtype=str)
    # print(sourceData.loc[:,["科目编码"]])
    # 大致筛选   
    dealData=sourceData.loc[(sourceData["科目编码"]=="6001020101") & (sourceData["摘要"].str.contains('Monthly Rent')) & (sourceData["摘要"].str.contains("北京致和康道生物科技有限公司")),:]
    dealData.reset_index(drop=True,inplace=True)
    dic={}
    
    for i in range(1,13):
        try:
            if i==int(dealData["月"][i-1]):
                dic[dealData["月"][i-1]]=dealData["贷"][i-1]
            else:
                dic[i]=0
        except :
            dic[i]=0
    # print(dealData.loc[(dealData["摘要"].str.contains("北京致和康道生物科技有限公司")),:])  
    print(dic)
work()    
