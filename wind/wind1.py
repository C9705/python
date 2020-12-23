import pandas as pd
import numpy as np
import os
import datetime
url='wind/wind.data'
data=pd.read_table(url,sep='\s+',parse_dates=[[0,1,2]])
print(data.head(2))
# 修复2061bug
def Bu(x):
    year = x.year-100 if x.year>1989 else x.year
    return datetime.date(year,x.month,x.day)
data['Yr_Mo_Dy']=data['Yr_Mo_Dy'].apply(Bu)
print(data.head(2))
# 日期设为索引，数据类型为datetime64
data['Yr_Mo_Dy']=pd.to_datetime(data['Yr_Mo_Dy'])
data=data.set_index('Yr_Mo_Dy',drop=True)
print(data.head(2))

#对应location的缺失值数量
print(data.isnull().sum()) 

# 对应location完整数据值
print(data.count())

# 计算全体数据风速的平均值
print(data.mean().mean())

# 创建loc_stats计算并存储location的最小值，最大值，平均值，标准差
loc_stats=pd.DataFrame()
loc_stats['min']=data.min()
loc_stats['max']=data.max()
loc_stats['mean']=data.mean()
loc_stats['std']=data.std()
print(loc_stats)

# day_stats存储所有location的min，max，mean，std
day_stats=pd.DataFrame()
day_stats['min']=data.min(axis=1)
day_stats['max']=data.max(axis=1)
day_stats['mean']=data.mean(axis=1)
day_stats['std']=data.std(axis=1)
print(day_stats)

# 每个location计算一月份的平均风速
data['date']=data.index
data['year']=data['date'].apply(lambda x:x.year)
data['month']=data['date'].apply(lambda x:x.month)
data['day']=data['date'].apply(lambda x:x.day)
print(data.query('month == 1').loc[:,'RPT':'MAL'].mean())

# 按年为频率进行取样
print(data.query('month == 1 and day == 1'))

# 按月进行取样
print(data.query('day == 1'))