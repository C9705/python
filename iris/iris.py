import pandas as pd
import numpy as np
iris=pd.read_csv('iris/iris.csv',names=['sepal_length','sepal_width', 'petal_length', 'petal_width', 'class'])
print(iris.head())
# 数据框中有缺失值吗？
print(iris.isnull().sum())
# 将petal_length的第10行到19行设置为缺失值
iris['petal_length'][9:20]=np.nan
# print(iris.head(21))
# 将缺失值全部替换为1.0
iris['petal_length']=iris['petal_length'].fillna(1.0)
print(iris.head(21))
# 删除列class
del iris['class']
print(iris.head())
# 将前三行设置为缺失值
iris.iloc[:3,]=np.nan
print(iris.head())
# 删除有缺失值的行
iris.dropna(axis=0,how='any',inplace=True)
# 重置索引
iris.reset_index(drop=True,inplace=True)
print(iris.head())
# 