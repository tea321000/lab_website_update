import os

from docx import Document
from yattag import Doc
from config import web_page_base, subject_path
from bs4 import BeautifulSoup

subject_doc = Document(subject_path)

doc, tag, text, line = Doc().ttl()
with tag('table', klass='table table-striped table-hover', style='width:100%'):
    for table in subject_doc.tables:
        for row in table.rows:
            with tag('tr'):
                for cell in row.cells:
                    with tag('th', klass='text-center'):
                        text(cell.text)
soup = BeautifulSoup(open(os.path.join(web_page_base, 'subject.html'), 'rb'), 'lxml')
table = soup.find("div", class_="container table-responsive")
table.clear()
table.append(BeautifulSoup(doc.getvalue(), 'html.parser'))
with open(os.path.join(web_page_base, 'subject.html'), 'wb') as f:
    f.write(soup.encode('utf-8'))

