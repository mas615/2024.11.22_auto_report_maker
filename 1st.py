# 가장 기본적인 기능(문서 열기, 저장, 글자 쓰기 등등)
from docx import Document

# 문단 정렬
from docx.enum.text import WD_ALIGN_PARAGRAPH

# 문자 스타일 변경
from docx.enum.style import WD_STYLE_TYPE

#워드문서 생성
doc = Document('최초진단.docx')

# 현재 작업경로에 저장
doc.save('최초진단2.docx')
