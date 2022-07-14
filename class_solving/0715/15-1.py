# 문자열 word가 주어질 때, 해당 문자열에서 a 의 모든 위치(index)를 출력해주세요.
# find() index() 메서드 사용 금지
# Input : HappyHacking / Output : 1 6

# 1. 리스트에 담기
# 그때그때 출력하지 않고 담아둬야 하는 경우, 리스트에 담는 방법이 유리
word = 'banana'
result = [] 
# result 라는 리스트를 먼저 생성해줌
for i in range(len(word)):
    if word[i] == 'a':
        # 리스트에 추가해줘
        result.append(i)
print(result)

# 2. 그때 그때 출력
word = 'banana'
result = []
for i in range(len(word)):
    if word[i] == 'a':
        print(i, end=' ')