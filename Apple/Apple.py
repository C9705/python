import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

url='Apple/Apple_stock.csv'
apple=pd.read_csv(url)
print(apple.head())
# 查看每一列的数据类型
print(apple.dtypes)
# 将Date转换成datetime类型
apple['Date']=pd.to_datetime(apple['Date'])
print(apple.dtypes)
# 将Date设置为索引
apple=apple.set_index('Date')
print(apple.head())
# 有重复的日期吗？
print(np.sum(apple.index.duplicated()))
# 将index设置为升序
print(apple.sort_index(ascending = True,axis=0).head())
# print(apple)
#找到每个月最后一个交易日business day
print('-----------------')
print(apple.resample('BM').last())

# 数据中最早的日期和最晚的日期相差多少天
day=(apple.index.max()-apple.index.min()).days
print(day)

# 在数据中一共有多少个月
da=pd.DataFrame()
da['Year']=apple.index
Month=da['Year'].apply(lambda x:x.month)
print(Month.nunique())
# 按时间顺序可视化Adj Close
plt.plot(apple.index,apple['Adj Close'])
plt.show()
