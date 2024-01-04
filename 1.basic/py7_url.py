from urllib.request import urlopen


def test_url():
    print("URL---------------------")

    baidu = urlopen("http://www.baidu.com")
    print(baidu.read(100))


test_url()
