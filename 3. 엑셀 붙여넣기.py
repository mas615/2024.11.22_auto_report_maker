import pandas as pd
import io

# 사용자 입력 받기 (엑셀처럼 붙여넣기)
print("엑셀 데이터를 복사해서 붙여넣으세요 (입력이 끝나면 엔터 2번):")
input_data = ""
while True:
    line = input()
    if line.strip() == "":
        break
    input_data += line + "\n"

# 데이터프레임 변환
try:
    df = pd.read_csv(io.StringIO(input_data), sep="\t")  # 탭 구분 데이터 처리
    print(df)
except Exception as e:
    print("입력 데이터를 처리하는 데 실패했습니다:", e)
