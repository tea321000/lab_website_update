import os
from yattag import Doc
from config import web_page_base, student_item_path
from bs4 import BeautifulSoup

# 需事先将照片放到student_item_path下，命名格式:degree_name.extension
soup = BeautifulSoup(open(os.path.join(web_page_base, 'student_list.html'), 'rb'), 'lxml')
item_list = soup.find("ul", id='portfolio-container')
# 获取图片与根目录的相对路径
item_relpath = os.path.relpath(student_item_path, web_page_base)
# 获取teacher_item_path和teacher_photo_path下的文件列表
photos = [f for f in os.listdir(student_item_path) if os.path.isfile(os.path.join(student_item_path, f))]
degree_dict = {'本科': 'undergraduate', '硕士': 'master', '博士': 'phd', '毕业': 'graduate', '毕业博士': 'graduate'}
doc, tag, text, line = Doc().ttl()
photo_dict = {}
for photo in photos:
    degree, name = os.path.splitext(photo)[0].split('_')
    if degree not in photo_dict:
        photo_dict[degree] = []
    photo_dict[degree].append(photo)

# print(photo_dict)
order = ['博士', '硕士', '本科', '毕业博士', '毕业']
for item in order:
    for photo in photo_dict[item]:
        degree, name = os.path.splitext(photo)[0].split('_')
        category = degree_dict[degree]
        if degree == '毕业':
            degree = '毕业硕士'
        with tag('li', ('class', 'isotope-item'), ('data-categories', category)):
            with tag('div', klass='item-wrapp'):
                with tag('div', klass='portfolio-item'):
                    with tag('a', ('class', 'item-preview'), ('data-rel', 'prettyPhoto'),
                             ('href', os.path.join(item_relpath, photo))):
                        with tag('i', klass='icon-zoom-in'):
                            pass
                    doc.stag('img', src=os.path.join(item_relpath, photo), alt=photo)
                with tag('div', klass='portfolio-item-title'):
                    with tag('a', href='#'):
                        text(name)
                    line('p', degree)

print(doc.getvalue())
item_list.clear()
item_list.append(BeautifulSoup(doc.getvalue(), 'html.parser'))
with open(os.path.join(web_page_base, 'student_list.html'), 'wb') as f:
    f.write(soup.encode('utf-8'))
