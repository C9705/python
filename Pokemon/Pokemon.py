import pandas as pd
import numpy as np
raw_data = {"name": ['Bulbasaur', 'Charmander','Squirtle','Caterpie'],
            "evolution": ['Ivysaur','Charmeleon','Wartortle','Metapod'],
            "type": ['grass', 'fire', 'water', 'bug'],
            "hp": [45, 39, 44, 45],
            "pokedex": ['yes', 'no','yes','no']                        
            }

#  将数据字典存为一个名叫pokemon的数据框中
pokemon=pd.DataFrame(raw_data)
print(pokemon.head())
# 将数据框列排序，按字母排序
pokemon=pokemon[['name','type','hp','evolution','pokedex']]
print(pokemon.head())
# 添加一列place
pokemon['place']=['park','street','lake','forest']
print(pokemon)
# 查看每个列的数据类型
print(pokemon.info())
print(pokemon.dtypes)
