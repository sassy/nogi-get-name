import urllib.request
from bs4 import BeautifulSoup

def main():
    url = 'http://www.nogizaka46.com/member/'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html, "html.parser")
    units = soup.find_all("div", {"class": "unit"})
    for unit in units:
        if unit.find('span',  {"class": "main"}) is not None:
            print(unit.find('span',  {"class": "main"}).string)

if __name__ == '__main__':
    main()
