import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn  as sns
# 显示中文
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

pd.set_option('display.width',None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
titanic=pd.read_csv('View/train.csv')
print(titanic.head())
#将passengerId设为索引
titanic=titanic.set_index('PassengerId',drop=True)
print(titanic.head())
# 绘制展现男女比例的扇形图
male=titanic.loc[titanic['Sex']=='male',['Sex']].count()
female=titanic.loc[titanic['Sex']=='female',['Sex']].count()
fig=plt.figure(figsize=(8,6),dpi=80)
frac=[male,female]
labels=['male','female']
plt.pie(frac,labels=labels,autopct="%.1f%%")
plt.title('男女比例')
plt.show()

# 绘制船票Fare与乘客年龄，性别的散点图
dataMale=titanic.loc[titanic['Sex']=='male',:]
dataFemale=titanic.loc[titanic['Sex']=='female',:]
# print(dataMale)
fareMale=dataMale['Fare'].values
ageMale=dataMale['Age'].values
fare=dataFemale['Fare'].values
age=dataFemale['Age'].values
plt.scatter(ageMale,fareMale,marker='o',label="男")
plt.scatter(age,fare,marker='^',label="女")
plt.legend(loc='best')
plt.show()
# 有多少人生还
print(titanic.Survived.sum())

# 展现船票的直方图
df=titanic.Fare.sort_values(ascending=False)
plt.hist(df)
plt.show()
