import requests
from bs4 import BeautifulSoup
from pandas import DataFrame


def first_try():
    headers = {'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)"
               " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36 Edg/121.0.0.0"}
    response = requests.get("https://www.runoob.com/html/html-intro.html", headers=headers)

    print(response.status_code)
    # print(response.text)

    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.prettify())
    # print(soup.get_text())
    links = []
    for link in soup.find_all('a'):
        links.append(link)
    print(len(links))
    # for lnk in links[:10]:
    #     print(lnk)

    # print(soup.p['class'])
    # print(soup.title)
    # print(soup.title.string)
    # print(soup.a)
    # print(soup.a.string)

    print(soup.select('#content > h2:nth-child(3)')[0].get_text())


def get_rmb_price():
    headers = {'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)"
               " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36 Edg/121.0.0.0"}
    res = requests.get("https://www.jyshare.com/rmbquot/", headers=headers)
    print(res.status_code)

    # soup = BeautifulSoup(res.text, 'html.parser')
    soup = BeautifulSoup(res.text, 'lxml')
    nations = ['body > div.runoob-home-main.mt-1 > div > div:nth-child(1) >'
               ' div.col-md-12.nav-moredata > div > table > tbody > tr:nth-child({}) > td:nth-child(1) > a'
               .format(n) for n in range(1, 22)]
    buy1 = ['body > div.runoob-home-main.mt-1 > div > div:nth-child(1) >'
            ' div.col-md-12.nav-moredata > div > table > tbody > tr:nth-child({}) > td:nth-child(2)'
            .format(n) for n in range(1, 22)]
    buy2 = ['body > div.runoob-home-main.mt-1 > div > div:nth-child(1) >'
            ' div.col-md-12.nav-moredata > div > table > tbody > tr:nth-child({}) > td:nth-child(3)'
            .format(n) for n in range(1, 22)]
    ns, b1s, b2s = [], [], []
    for nation, b1, b2 in zip(nations, buy1, buy2):
        ns.append(soup.select(nation)[0].get_text())
        b1s.append(soup.select(b1)[0].get_text())
        b2s.append(soup.select(b2)[0].get_text())
        # print(soup.select(nation)[0].get_text(), soup.select(b1)[0].get_text(), soup.select(b2)[0].get_text())

    df = DataFrame({"现汇": b1s, "现钞": b2s}, index=ns) 
    print(df)


get_rmb_price()
