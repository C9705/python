import pandas as pd
import numpy as np
import os
# 数据地址
url="US/us.csv"
# crime读取
crime=pd.read_csv(url,encoding='utf-8')
print(crime.head(2))
# 查看每一列的数据类型
print(crime.info())
# 将year的数据类型转换为datetime64
# pd.to_datetime()修改成日期数据类型
crime['Year']=pd.to_datetime(crime['Year'],format='%Y')
print(crime.info())
# 将Year设置为索引
crime = crime.set_index('Year', drop = True)
print(crime.index)
print(crime.head(5))

# 删除total的列
crime.drop('Total',axis=1,inplace=True)
print(crime.info())

# 按Year对数据进行分组求和
# crime.groupby('Year').apply(np.sum)
# print(crime.groupby('Year').apply(np.sum))
# 对Year进行整合，10年一组
# resample()进行10年一组
crimes=crime.resample('10AS').sum()
population = crime['Population'].resample('10AS').max()
crimes['Population'] = population
print(crimes)
# 何时是美国历史上生存最危险的年代？
print(crime.idxmax(0))
print(crime.idxmax())