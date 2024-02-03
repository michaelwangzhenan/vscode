import json
import pandas as pd
from pandas import DataFrame


def test_data():
    db = json.load(open("7.data_analysis/data/usda_food.json"))
    print(type(db))  # db 是一个列表
    print(len(db))
    print(type(db[0]))  # 每一项是一个数据字典
    print(db[0].keys())  # 每数据字典的 keys

    print("id=", db[0]['id'])
    print("description=", db[0]['description'])
    print("tags=", db[0]['tags'])
    print("manufacturer=", db[0]['manufacturer'])
    print("group=", db[0]['group'])
    print("portions=", db[0]['portions'])

    print("len of nutrients=", len(db[0]['nutrients']))
    print("nutrients[0]=", db[0]['nutrients'][0])
    print("nutrients[123]=", db[0]['nutrients'][123])

    df_nutrients = DataFrame(db[0]['nutrients'])
    print(df_nutrients)

    df_info = DataFrame(db, columns=['id', 'description', 'group'])
    print(df_info)
    print(pd.value_counts(df_info['group']))


def handle_data():
    db = json.load(open("7.data_analysis/data/usda_food.json"))
    nutrients = []
    for rec in db:
        df_nutrients = DataFrame(rec['nutrients'])
        df_nutrients['id'] = rec['id']
        nutrients.append(df_nutrients)

    nutrients = pd.concat(nutrients, ignore_index=True)
    # print(len(nutrients))
    print(nutrients.duplicated().sum())
    nutrients = nutrients.drop_duplicates()
    # print(len(nutrients))
    # print(nutrients[:10])

    df_info = DataFrame(db, columns=['id', 'description', 'group'])
    col_mapping = {'description': 'food_name', 'group': 'food_group'}
    df_info = df_info.rename(columns=col_mapping, copy=False)
    # print(df_info[:5])
    # print(df_info.index.size)

    ndata = pd.merge(nutrients, df_info, on='id', how='outer')
    print(ndata)


handle_data()
