import os

from docx import Document
from yattag import Doc
from config import web_page_base, journal_path
from bs4 import BeautifulSoup

journal_doc = Document(journal_path)

doc, tag, text, line = Doc().ttl()
with tag('table', klass='table table-striped table-hover', style='width:100%'):
    with tag('thread'):
        with tag('tr'):
            with tag('th', klass='col-sm-1 text-center'):
                text('序号')
            with tag('th', klass='col-sm-10 text-center'):
                text('名称')
            with tag('th', klass='col-sm-1 text-center'):
                text('索引')
    for table in journal_doc.tables:
        for row in table.rows:
            with tag('tr'):
                for cell in row.cells:
                    with tag('th', klass='text-center'):
                        text(cell.text)
soup = BeautifulSoup(open(os.path.join(web_page_base, 'journal.html'), 'rb'), 'lxml')
table = soup.find("div", class_="container table-responsive")
table.clear()
table.append(BeautifulSoup(doc.getvalue(), 'html.parser'))
with open(os.path.join(web_page_base, 'journal.html'), 'wb') as f:
    f.write(soup.encode('utf-8'))

