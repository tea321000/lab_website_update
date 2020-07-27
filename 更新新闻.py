import os

from config import web_page_base, latest_photo_path, latest_item_path, latest_link_path
from bs4 import BeautifulSoup

thumbs_photos = [f for f in os.listdir(latest_item_path) if os.path.isfile(os.path.join(latest_item_path, f))]
photos = [f for f in os.listdir(latest_photo_path) if os.path.isfile(os.path.join(latest_photo_path, f))]
item_relpath = os.path.relpath(latest_item_path, web_page_base)
photo_relpath = os.path.relpath(latest_photo_path, web_page_base)
with open(latest_link_path) as f:
    content = f.readlines()
content = [x.strip() for x in content]

soup = BeautifulSoup(open(os.path.join(web_page_base, 'index.html'), 'rb'), 'lxml')
for index, item in enumerate(soup.find_all("div", class_='one-fourth')):
    name = os.path.splitext(photos[index])[0].split('_')[1:][0]
    link = item.find('a', class_='item-permalink')
    link['href'] = content[index]
    photo = item.find('a', class_='item-preview')
    photo['href'] = os.path.join(photo_relpath, photos[index])
    item.img['src'] = os.path.join(item_relpath, thumbs_photos[index])
    title = item.find('div', class_='portfolio-item-title')
    title.a['href'] = content[index]
    title.a.string = name
    title.p.clear()

with open(os.path.join(web_page_base, 'index.html'), 'wb') as f:
    f.write(soup.encode('utf-8'))
