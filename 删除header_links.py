import os

from config import web_page_base
from bs4 import BeautifulSoup


soup = BeautifulSoup(open(os.path.join(web_page_base, 'index.html'), 'rb'), 'lxml')
navigation = soup.find("div", id='main-navigation')

modify_set=set()
# 寻找不是Index.html的link加入到set中
for link in navigation.find_all('a'):
    href=link.get('href')
    if href.find('.html')!=-1 and href!='index.html':
        modify_set.add(href)

for href in modify_set:
    modify_soup = BeautifulSoup(open(os.path.join(web_page_base, href), 'rb'), 'lxml')
    header = modify_soup.find("div", id="header-links")
    header.decompose()
    with open(os.path.join(web_page_base, href), 'wb') as f:
        f.write(modify_soup.encode('utf-8'))


