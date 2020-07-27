import os

from config import web_page_base
from bs4 import BeautifulSoup


soup = BeautifulSoup(open(os.path.join(web_page_base, 'index.html'), 'rb'), 'lxml')
footer = soup.find("footer", id="footer")
copyrights = soup.find("section", id='copyrights')
navigation = soup.find("div", id='main-navigation')


modify_set=set()
# 寻找不是Index.html的link加入到set中
for link in navigation.find_all('a'):
    href=link.get('href')
    if href.find('.html')!=-1 and href!='index.html':
        modify_set.add(href)
#
for href in modify_set:
    modify_soup = BeautifulSoup(open(os.path.join(web_page_base, href), 'rb'), 'lxml')
    modify_footer = modify_soup.find("footer", id="footer")
    modify_copyrights = modify_soup.find("section", id='copyrights')
    modify_footer.replaceWith(footer)
    modify_copyrights.replaceWith(copyrights)
    with open(os.path.join(web_page_base, href), 'wb') as f:
        f.write(modify_soup.encode('utf-8'))

teacher_soup = BeautifulSoup(open(os.path.join(web_page_base, 'teacher_list.html'), 'rb'), 'lxml')
item_list = teacher_soup.find("ul", id='portfolio-container')
for item in item_list.find_all('div', class_='item-wrapp'):
    title = item.find('div', 'portfolio-item-title')
    name = title.a.string
    modify_soup = BeautifulSoup(open(os.path.join(web_page_base, name+'.html'), 'rb'), 'lxml')
    modify_footer = modify_soup.find("footer", id="footer")
    modify_copyrights = modify_soup.find("section", id='copyrights')
    modify_footer.replaceWith(footer)
    modify_copyrights.replaceWith(copyrights)
    with open(os.path.join(web_page_base, name+'.html'), 'wb') as f:
        f.write(modify_soup.encode('utf-8'))
