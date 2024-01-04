import json


def test_json():
    # Python 字典类型转换为 JSON 对象
    data = {
        'No': 1,
        'Name': 'Runoob',
        'Url': 'http://www.runoob.com'
        }

    json_str = json.dumps(data)  # 返回一个json str,不能写文件
    loads = json.loads(json_str)  # 从 json str 中读取
    print("data : ", data)
    print("json : ", json_str)
    print("loads : ", loads)

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


test_json()
