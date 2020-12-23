# 探索Chipotle快餐数据
# 导入库
import pandas as pd
import numpy as np
# 设置查看
pd.set_option('display.width',None)
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
# 导入数据集
url="chipotle.tsv"
# 读取数据集,sep为分隔符
chipo=pd.read_csv(url, sep = '\t')
# 读取前10行
# 数据分别为订单id，数量，名字，选择，价格
print(chipo.head(10))
print('---------------------------------')
#查看数据集中有多少列--shape返回行列数
print(chipo.shape[1])
print('---------------------------------')
# 打印全部列名称
print(chipo.columns)
print('---------------------------------')
# 数据集的索引是怎么样的
print(chipo.index)
print('---------------------------------')
# 被下单数最多的商品是什么
# 运用groupby进行分组，其中as_index=False，会输出索引，agg/apply分组聚合函数
# sort_values进行排序，ascending=False，为降序
c=chipo[['item_name','quantity']].groupby(['item_name'],as_index=False).agg({'quantity':np.sum})
c.sort_values(['quantity'],ascending=False,inplace=True,)
print(c.head())
print('---------------------------------')
# 在item_name中，一共有多少商品被下单
# nunique()--返回唯一值的个数
cNum=chipo['item_name'].nunique()
print(cNum)
print('---------------------------------')
#在choice_description中，下单次数最多的商品是什么？   
#   value_counts()计数
print(chipo['choice_description'].value_counts().head())
print('---------------------------------')

# 一共有多少商品被下单
print(chipo['quantity'].sum())
print('---------------------------------')
# 将item_price转换为浮点型, 
# dtype查看数据类型
chipo['item_price']=chipo['item_price'].apply(lambda x: float(x[1:]))
print(chipo['item_price'].dtype)
# 在改数据集对应的时期内，收入（revenue）是多少
# np.dot(),对应乘积
revenue=round(np.dot(chipo['quantity'],chipo['item_price']),2)
print(revenue)
chipo['sub_total']=revenue
print('---------------------------------')
# 在数据集对应期内，共有多少订单
print(chipo['order_id'].nunique())
print('---------------------------------')
# 每一单order对应的平均总价是多少

men=chipo[['order_id','sub_total']].groupby('order_id').agg({'sub_total':np.sum})['sub_total'].mean()
men=chipo[['order_id','sub_total']].groupby(by=['order_id']).agg({'sub_total':'sum'})['sub_total'].mean()
print(round(men,2))

print(revenue/chipo['order_id'].nunique())
print('---------------------------------')
# 一共有多少种不同的商品被售出
chipo['item_name'].nunique()
print('---------------------------------')