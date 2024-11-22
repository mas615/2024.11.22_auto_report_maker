import pandas as pd
import io
import pyperclip
#GUI 관련
import tkinter as tk
from tkinter import ttk
import io  # StringIO를 위한 모듈

# 클립보드에서 데이터를 읽어오기
clipboard_data = pyperclip.paste()

# 데이터를 판다스 데이터프레임으로 변환
def csvpaste():
    try:
        df = pd.read_csv(io.StringIO(clipboard_data), sep="\t")  # 복사된 데이터를 탭으로 구분
        # print(type(df))
        # print(df)

        # '내용' 열 선택
        #column_data = df['내용']

        # 첫 번째 행 선택
        row_data = df.iloc[0]

        # 첫 번째 행, 두 번째 열의 값
        cell_value = df.iloc[0, 5]

        print(cell_value)
        return True

    except Exception as e:
        print("클립보드 데이터를 처리하는 데 실패했습니다:", e)
        return False

def display_table():
    root = tk.Tk()
    root.title("SK C&C Ma_nager")
    label = Label(root, text='Hello World')
    frame = ttk.Frame(root, width=640, height=320).grid()
    ttk.Button(frame, text="Hello World").grid(column=0, row=0)
    root.mainloop()


def errorcheckpaste():
    #input('복사 후 엔터를 누르세요')
    # a = csvpaste()
    # print(a)
    display_table()









def main():
    # 여기에 프로그램의 주요 로직 작성
    print("----------------------SK C&C 보고서 자동완성----------------------")
    errorcheckpaste()

if __name__ == "__main__":
    main()
