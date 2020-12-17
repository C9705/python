import pandas as pd
import numpy as np

# 导入
euro12=pd.read_csv('Euro2012_stats.csv')
print(euro12.head(5))

# 1.只选取Goals这一列
Goals=euro12.loc[:,'Goals']

# 2.有多少球队参与了2012欧洲杯
print(euro12['Team'].count())
# 3.数据集共有多少列
print(euro12.shape[1])
euro12.info()
# 4.将team，Yellow Cards和Red Cards单独为discipline的数据集中
discipline=euro12.loc[:,['Team','Yellow Cards','Red Cards']]
print(discipline.head(2))
# 5.对discipline先red后yellow进行排序
discipline.sort_values(['Red Cards','Yellow Cards'],ascending=False,inplace=True)
print(discipline.head(2))
# 6.计算每个球队拿到黄牌的平均值
yellowMean=discipline['Yellow Cards'].sum()/discipline['Team'].count()
round(discipline['Yellow Cards'].mean())
print(yellowMean)
# 7.找到进球数Goals超过6的球队数据
print(euro12.loc[euro12['Goals']>6,:])
euro12[euro12.Goals > 6]
# 8.选取以G开头的球队数据
print(euro12.loc[euro12['Team'].apply(lambda x:x[0].title()=="G"),:])
euro12[euro12.Team.str.startswith('G')]
# 9.选取前7列
print(euro12.iloc[:,0:7])
# 10.选取除了最后3列之外的全部列
print(euro12.iloc[:,0:-4])
# 11.找到英格兰，意大利，俄罗斯的射正率
sTeamData=euro12.loc[euro12['Team'].isin(['England', 'Italy', 'Russia']),['Team','Shooting Accuracy']]
print(sTeamData)
