import json
from pprint import pprint


def test_json():
    # Python 字典类型转换为 JSON 对象
    data = {
        'No': 1,
        'Name': 'Runoob',
        'Url': 'http://www.runoob.com'
        }

    json_str = json.dumps(data)  # dict 转成 str
    loads = json.loads(json_str)  # str 转成 dict

    print("type=", type(data), "content : ", data)
    print("type=", type(json_str), "content : ", json_str)
    print("type=", type(loads), "content : ", loads)

    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)  # 将json 对象写入文件

    with open('data.json', 'r') as f:
        json_file = json.load(f)  # 从文件中读取 json 数据
    print("file : ", json_file)

    with open('data.json', 'r+') as f:
        data['Note'] = 'this is a note'
        json.dump(data, f, indent=4)
        f.seek(0)
        json_note = json.load(f)
    print("note : ", json_note)
    pprint(json_note)  # better print format


test_json()


# TODO
# pandas.read_json
# pandas.DataFrame.to_json
# pandas.Series.to_json
