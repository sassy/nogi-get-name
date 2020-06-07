import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import sys

base_url = 'http://www.nogizaka46.com/member/'

def get_html():
    req = urllib.request.Request(base_url, headers={'User-Agent': 'Mozilla/5.0'})
    return urllib.request.urlopen(req).read()

def namelist():
    html = get_html()
    soup = BeautifulSoup(html, "html.parser")
    units = soup.find_all("div", {"class": "unit"})
    for unit in units:
        if unit.find('span',  {"class": "main"}) is not None:
            kanji = unit.find('span',  {"class": "main"}).string
            kana = unit.find('span',  {"class": "sub"}).string if unit.find('span',  {"class": "sub"}) is not None else unit.find('span',  {"class": "sub2"}).string
            print(kanji + " " + kana )

def namelist_with_birthday():
    html = get_html()
    soup = BeautifulSoup(html, "html.parser")
    units = soup.find_all("div", {"class": "unit"})
    for unit in units:
        if unit.find('span',  {"class": "main"}) is not None:
            kanji = unit.find('span',  {"class": "main"}).string
            kana = unit.find('span',  {"class": "sub"}).string if unit.find('span',  {"class": "sub"}) is not None else unit.find('span',  {"class": "sub2"}).string
            url = urljoin(base_url, unit.find('a')['href'])
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            next_html = urllib.request.urlopen(req).read()
            soup2 = BeautifulSoup(next_html, "html.parser")
            birthday = soup2.find_all("dd")[0].string
            print(kanji + " " + kana + " " + birthday)
            #print('{ name: "' + kana + '", birthday: "' + birthday + '" },')

def main():
    arguments = sys.argv
    if len(arguments) > 1 and '-b' in arguments[1]:
        namelist_with_birthday()
    else:
        namelist()

if __name__ == '__main__':
    main()
