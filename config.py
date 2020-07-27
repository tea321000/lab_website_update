import os

# "I:\\OneDrive - email.szu.edu.cn\\实验室网站\\网站内容\\研究成果\\期刊\\期刊.docx"
doc_base = os.path.join('I:', os.sep, 'OneDrive - email.szu.edu.cn', '实验室网站', '网站内容')
web_page_base = os.path.join('I:', os.sep, 'OneDrive - email.szu.edu.cn', '实验室网站', '感知实验室')
research_base = os.path.join(doc_base, '研究成果')
lab_base = os.path.join(doc_base, '实验室概况')
journal_path = os.path.join(research_base, '期刊', '期刊.docx')
conference_path = os.path.join(research_base, '会议', '会议.docx')
patent_path = os.path.join(research_base, '专利', '专利.docx')
prize_path = os.path.join(research_base, '获奖', '获奖.docx')
subject_path = os.path.join(lab_base, '相关课题', '相关课题.docx')
teacher_photo_path = os.path.join(web_page_base, 'images', 'portfolio')
teacher_item_path = os.path.join(teacher_photo_path, 'thumbs')
student_item_path = os.path.join(teacher_photo_path, 'students')
latest_photo_path = os.path.join(web_page_base, 'images', 'latest')
latest_item_path = os.path.join(latest_photo_path, 'thumbs')
latest_link_path = os.path.join(latest_photo_path, 'link','链接.txt')