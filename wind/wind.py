import pandas as pd
import numpy as np
import os
import datetime
url='wind/wind.data'
# parse_dates:将数据解析成日期

# 将数据前三列作为所以
data=pd.read_table(url,sep='\s+',parse_dates=[[0,1,2]])
print(data.head())
# 创建一个函数，修改2061年这个bug年份
def fix_century(x):
    year = x.year - 100 if x.year > 1989 else x.year
    return datetime.date(year, x.month, x.day)
data['Yr_Mo_Dy']=data['Yr_Mo_Dy'].apply(fix_century)
print(data.head())

# 设置日期为索引，数据类型为datetime64
data['Yr_Mo_Dy']=pd.to_datetime(data['Yr_Mo_Dy'])
data=data.set_index('Yr_Mo_Dy',drop=True)
print(data.head())
# 每一个location，一共有多少个数据缺失值
print(data.isnull().sum())

# 对应location ，一共有多少完整的数据
print(data.count())

#对于全体数据，计算风速的平均值
print(data.mean().mean()) 

# 创建一个名为loc_stats的数据框去计算并存储每个location的风速最小值，最大值，平均值，标准差
loc_stats = pd.DataFrame()
loc_stats['min'] = data.min() # min
loc_stats['max'] = data.max() # max 
loc_stats['mean'] = data.mean() # mean
loc_stats['std'] = data.std() # standard deviations
print(loc_stats)

# 对于每个location，计算一月份的平均风速
data['date']=data.index
data['Year']=data['date'].apply(lambda x:x.year)
data['Month']=data['date'].apply(lambda x:x.month)
data['Day']=data['date'].apply(lambda x:x.day)
x=data.loc[data['Month']==1,:].mean()
print(data)
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
print(x)

# 对于数据记录按照年为频率取样
data.query('month == 1 and day == 1')
# 对于数据记录按照月为频率取样
data.query('day == 1')