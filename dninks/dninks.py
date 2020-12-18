import pandas as pd
import numpy as np
pd.set_option('display.width',None)
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
# 探索酒类消费数据
url='E:\Python\dninks\drinks.csv'
# 读取数据
drinks = pd.read_csv(url)
print(drinks.head(3))
# 哪个大陆（continent）平均消耗啤酒beer更多？
print('----------------哪个大陆（continent）平均消耗啤酒beer更多？------------------')
sumBeer=drinks[['continent','beer_servings']].groupby('continent',as_index=False).agg({'beer_servings':np.mean})
sumBeer.sort_values(['beer_servings'],ascending=False,inplace=True)
sumBeer.reset_index(drop=True,inplace=True)
print(sumBeer)
print(sumBeer['continent'][0])
# 打印出每个大陆(continent)的红酒消耗(wine_servings)的描述性统计值describe
print('--------------打印出每个大陆(continent)的红酒消耗(wine_servings)的描述性统计值describe--------------------')
wine=drinks.groupby('continent').wine_servings.describe()
print(wine)

# 打印出每个大陆每种酒类别的消耗平均值
print('--------------打印出每个大陆每种酒类别的消耗平均值--------------------')
print(drinks.groupby('continent').mean())

# 打印出每个大陆每种酒类别的消耗中位数
print('--------------打印出每个大陆每种酒类别的消耗中位数--------------------')
print(drinks.groupby('continent').median())

# 打印出每个大陆对spirit饮品消耗的平均值，最大值和最小值
print('--------------打印出每个大陆对spirit饮品消耗的平均值，最大值和最小值--------------------')
print(drinks.groupby('continent').spirit_servings.describe())