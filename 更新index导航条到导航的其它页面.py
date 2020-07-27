import os

from config import web_page_base
from bs4 import BeautifulSoup, NavigableString, Tag

soup = BeautifulSoup(open(os.path.join(web_page_base, 'index.html'), 'rb'), 'lxml')
logo = soup.find("div", class_="head-wrapp")
title = soup.title.string
navigation = soup.find("div", id='main-navigation')
menu = soup.find("ul", class_='main-menu')


modify_dict = dict()
# 寻找直接子节点一级目录
for child in menu.children:
    if isinstance(child, NavigableString):
        continue
    if isinstance(child, Tag):
        father=child.contents[0].get('href')
        if father!='index.html':
            if child.ol!=None:
                for ol_list in child.find_all('ol'):
                    # 多级列表需要再往下遍历一层
                    for link in ol_list.find_all('a'):
                        # print('ol:',link)
                        if link.get('href') not in modify_dict:
                            # 键值分别为{子节点链接：父节点链接}
                            modify_dict[link.get('href')]=father
            elif child.ul!=None:
                for link in child.ul.find_all('a'):
                    # print('ul:', link)
                    if link.get('href') not in modify_dict:
                        modify_dict[link.get('href')]=father
            else:
                # 没有子节点则父节点为自身
                modify_dict[father] = father

# print(modify_dict)
#
for href in modify_dict:
    modify_soup = BeautifulSoup(open(os.path.join(web_page_base, href), 'rb'), 'lxml')
    modify_soup.title.string = title
    modify_logo = modify_soup.find("div", class_="head-wrapp")
    modify_navigation = modify_soup.find("div", id='main-navigation')
    modify_logo.replaceWith(logo)
    modify_navigation.replaceWith(navigation)
    modify_current = modify_soup.find("a", id='current')
    if modify_current!=None:
        del modify_current['id']
    modify_menu = modify_soup.find("ul", class_='main-menu')
    # 寻找新的设置current的一级目录
    for child in modify_menu.children:
        if isinstance(child, NavigableString):
            continue
        if isinstance(child, Tag):
            if child.contents[0].get('href')==modify_dict[href]:
                child.contents[0]['id']='current'
                break
    with open(os.path.join(web_page_base, href), 'wb') as f:
        f.write(modify_soup.encode('utf-8'))

teacher_soup = BeautifulSoup(open(os.path.join(web_page_base, 'teacher_list.html'), 'rb'), 'lxml')
teacher_soup.title.string = title
item_list = teacher_soup.find("ul", id='portfolio-container')

for item in item_list.find_all('div', class_='item-wrapp'):
    item_title = item.find('div', 'portfolio-item-title')
    name = item_title.a.string
    modify_soup = BeautifulSoup(open(os.path.join(web_page_base, name + '.html'), 'rb'), 'lxml')
    modify_logo = modify_soup.find("div", class_="head-wrapp")
    modify_navigation = modify_soup.find("div", id='main-navigation')
    modify_logo.replaceWith(logo)
    modify_navigation.replaceWith(navigation)
    header = modify_soup.find("div", id="header-links")
    if header!=None:
        header.decompose()
    teacher_current = modify_soup.find("a", id='current')
    if teacher_current != None:
        del teacher_current['id']
    teacher_menu = modify_soup.find("ul", class_='main-menu')
    for child in teacher_menu.children:
        if isinstance(child, NavigableString):
            continue
        if isinstance(child, Tag):
            # 老师页面的current父节点都是研究队伍
            if child.contents[0].get('href') == 'teacher_list.html':
                child.contents[0]['id'] = 'current'
                break
    with open(os.path.join(web_page_base, name + '.html'), 'wb') as f:
        f.write(modify_soup.encode('utf-8'))

