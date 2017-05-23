import requests
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit


def main():
    url_base = "https://bbs.pku.edu.cn/v2/"
    url = "https://bbs.pku.edu.cn/v2/collection.php?path=groups%2FGROUP_0%2FPersonalCorpus%2FD%2Fdigua%2Fguestbook%2FD97BEB239"
    cookies = {'skey':'163c247af2c1eef4','uid':'3988'}
    print(cookies)
    r = requests.get(url, cookies=cookies)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup.findAll("a", { "class" : "item-name" }))


if __name__ == "__main__":
    main()