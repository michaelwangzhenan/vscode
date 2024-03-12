import requests
import re
from bs4 import BeautifulSoup


def try_req(url):
    headers = {'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)"
               " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36 Edg/121.0.0.0"}

    res = 0
    counter = 0
    while res != 200 and counter < 100:
        response = requests.get(url, headers=headers)
        res = response.status_code
        counter = counter + 1
        response.encoding = 'utf-8'
        print(f'response={res}, tried={counter}, coding={response.encoding}')

    f = open("novel.txt", 'w+')
    contents = re.findall('<p>(.*?)</p>|<li>(.*?)</li>',  response.content.decode('utf-8'), re.S)
    for content in contents:
        # content = re.sub('&#x....', '', content)
        if content[0] != '':
            print(content[0])
            f.write(content[0] + '\n')
        else:
            print(content[1])
            f.write(content[1] + '\n')

    f.close()


url = 'https://blog.csdn.net/qq_41045651/article/details/131413530'
try_req(url)
