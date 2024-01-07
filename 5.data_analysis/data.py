import json
from collections import defaultdict, Counter


def convert_json():
    file = "5.data_analysis/data/eq_data_30_day_m1.json"
    with open(file) as f:
        content = json.load(f)
    f_file = file[0:len(file)-5] + '_formated' + file[-5:]
    with open(f_file, "w") as formated:
        json.dump(content['features'], formated, indent=4)


def count_tz():
    file = "5.data_analysis/data/bitly_usagov.txt"
    content = [json.loads(line) for line in open(file, "r", encoding='utf-8')]
    tzs = [item['tz'] for item in content if 'tz' in item and item['tz'] != '']
    set_tz = set(tzs)
    tz_count = []
    for data in set_tz:
        tz_count.append((data, tzs.count(data)))
    tz_count.sort(key=lambda i: i[1], reverse=True)
    print("count_tz", "="*100)
    print(tz_count[:10])


def count_tz2():
    file = "5.data_analysis/data/bitly_usagov.txt"
    content = [json.loads(line) for line in open(file, "r", encoding='utf-8')]
    tzs = [item['tz'] for item in content if 'tz' in item and item['tz'] != '']
    tz_count = defaultdict(int)
    for tz in tzs:
        tz_count[tz] += 1
    # print(tz_count[list(tz_count.keys())[0]])
    tz_list = [(count, addr) for addr, count in tz_count.items()]
    tz_list.sort(reverse=True)
    # tz_list.reverse()
    print("count_tz2", "="*100)
    print(tz_list[:10])


def count_tz3():
    file = "5.data_analysis/data/bitly_usagov.txt"
    content = [json.loads(line) for line in open(file, "r", encoding='utf-8')]
    tzs = [item['tz'] for item in content if 'tz' in item and item['tz'] != '']
    count = Counter(tzs)
    print("count_tz3", "="*100)
    print(count.most_common(10))


# count_tz()
# count_tz2()
# count_tz3()
