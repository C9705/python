import pandas as pd
import numpy as np
pd.set_option('display.width',None)
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
# 导入数据
# sep为分隔符
chipo=pd.read_csv("chipotle.tsv",sep="\t")
# 查看前十行
print(chipo.head(1))
#1.数据集中有多少个列
print('数据中共有{}列'.format(chipo.shape[1])) 
# 2.打印出全部的列名称
print('列名为{}'.format(chipo.columns.values)) 
# 3.数据集的索引是怎样的
print('索引为{}'.format(chipo.index))
# 4.被下单数最多的商品item是什么？
itemMaxCount=chipo[['quantity','item_name']].groupby(['item_name'],as_index=False).agg({'quantity':np.sum})
itemMaxCount.sort_values(['quantity'],ascending=False,inplace=True)
itemMaxCount.reset_index(drop=True,inplace=True)
print(itemMaxCount.head(2))
print('被下单数最多的商品为{}'.format(itemMaxCount['item_name'][0]))

# 5.在item_name这一列中，一共有多少中商品被下单？
itmeCount=chipo['item_name'].nunique()
print('一共有{}种商品被下单'.format(itmeCount))
# 6.在choice_description中下单次数最多的商品是什么？
choice=chipo['choice_description'].value_counts()
print(choice.head(1))
# 7.一共共有多少商品被下单
print('共有{}商品被下单'.format(chipo['quantity'].sum()))

# 8.将itme_price 转换为浮点类型
chipo['item_price']=chipo['item_price'].apply(lambda x:float(x[1:-1]))
print(chipo['item_price'][0])
# 9.在数据集对应期内，有多少收入（revenue）
revenue=np.dot(chipo['quantity'],chipo['item_price'])
chipo['revenue']=round(revenue,2)
print('收入为:', round(revenue,2))

# 10.在数据集对应时期，一共有多少订单？
print('共有{}个订单'.format(chipo['order_id'].nunique()))

# 11.每一单对应的平均总价是多少？
print('每一单的平均平均总价为{}'.format(revenue/chipo['order_id'].nunique()))

# 12.一共有多少中不同的商品售出
print(chipo['item_name'].nunique())
