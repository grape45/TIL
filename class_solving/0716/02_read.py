# 파일명, 어떤 모드로 열지,
# 인코딩을 설정
with open('students.txt', 'r', encoding='utf=8') as f:
    # 텍스트는 string 타입
    text = f.read()
    print(text, type(text))
    # string.split() => list 타입
    names = text.split()
    cnt = 0
    for name in names:
        # name : 첫 번째 시행 - 가민지
        # 언제? 마씨?
        if name.startswith('마'):
        # if name[0] == '마':
            cnt += 1
    print(cnt)