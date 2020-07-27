import os

from config import web_page_base, teacher_photo_path, teacher_item_path
from bs4 import BeautifulSoup

# 需事先将照片放到teacher_item_path和teacher_photo_path下
soup = BeautifulSoup(open(os.path.join(web_page_base, 'teacher_list.html'), 'rb'), 'lxml')
about_soup = BeautifulSoup(open(os.path.join(web_page_base, 'about-us.html'), 'rb'), 'lxml')
item_list = soup.find("ul", id='portfolio-container')
# 获取图片与根目录的相对路径
item_relpath = os.path.relpath(teacher_item_path, web_page_base)
photo_relpath = os.path.relpath(teacher_photo_path, web_page_base)
# 获取teacher_item_path和teacher_photo_path下的文件列表
thumbs_photos = [f for f in os.listdir(teacher_item_path) if os.path.isfile(os.path.join(teacher_item_path, f))]
photos = [f for f in os.listdir(teacher_photo_path) if os.path.isfile(os.path.join(teacher_photo_path, f))]
for item in item_list.find_all('div', class_='item-wrapp'):
    title = item.find('div', 'portfolio-item-title')
    name = title.a.string
    preview = item.find('a', class_='item-preview')
    img = item.find('img')
    # 找到带有名字的图片 更新大图
    for photo in photos:
        if name in photo:
            preview['href'] = os.path.join(photo_relpath, photo)
    # 找到带有名字的图片 更新缩略图
    for thumb in thumbs_photos:
        if name in thumb:
            img['src'] = os.path.join(item_relpath, thumb)
            # 更新实验室简介html的缩略图
            team_list = about_soup.find_all("div", class_='team-member')
            for member in team_list:
                if name == member.a.string:
                    member.img['src'] = os.path.join(item_relpath, thumb)

            thumbs_photos.remove(thumb)
            break
    for photo in photos:
        if name in photo:
            # 找到带有名字的图片 更新大图
            photo_soup = BeautifulSoup(open(os.path.join(web_page_base, name + '.html'), 'rb'), 'lxml')
            avatar = photo_soup.find('div', class_='avatar')
            avatar.img['src'] = os.path.join(photo_relpath, photo)
            with open(os.path.join(web_page_base, name + '.html'), 'wb') as f:
                f.write(photo_soup.encode('utf-8'))

with open(os.path.join(web_page_base, 'teacher_list.html'), 'wb') as f:
    f.write(soup.encode('utf-8'))
with open(os.path.join(web_page_base, 'about-us.html'), 'wb') as f:
    f.write(about_soup.encode('utf-8'))
