import pandas as pd
import tkinter as tk
from tkinter import ttk
import pyperclip
import io  # StringIO를 위한 모듈

def display_table(data):
    root = tk.Tk()
    root.title("표 출력")

    # 스타일 설정
    style = ttk.Style()
    style.theme_use("clam")  # 테마 변경 (clam, default 등 사용 가능)
    style.configure("Treeview", rowheight=25)

    # Treeview 생성
    tree = ttk.Treeview(root, columns=list(data.columns), show="headings")

    # 컬럼 설정
    for col in data.columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=100)  # 열 너비 조정

    # 데이터 삽입
    for index, row in data.iterrows():
        tree.insert("", "end", values=list(row))

    # 스크롤바 추가
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # Treeview 배치
    tree.pack(expand=True, fill="both")

    root.mainloop()


# 클립보드에서 데이터 읽기
clipboard_data = pyperclip.paste()

# 헤더 없는 데이터를 처리
df = pd.read_csv(io.StringIO(clipboard_data), sep="\t", header=None)

# 컬럼 이름 수동 설정 (필요시 수정)
df.columns = ["대상", "URL", "관리코드", "취약점", "위험도", "내용", "발생위치", "시작일", "종료일", "조치상태"]  # 적절한 이름으로 수정

# GUI로 출력
display_table(df)
