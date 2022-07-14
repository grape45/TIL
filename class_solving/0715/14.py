# 문자열 word가 주어질 때, 해당 문자열에서 a 개수를 구하세요.
# count() 메서드 사용 금지

# input : apple / Output : 1

# 'apple' , a 카운트
word = 'apple'

# char는 이름 붙이기
# word의 요소를 하나씩 char 바인딩
count = 0
for char in word:
    if char == 'a':
        # a일ㄸ마다 +1
        count += 1
print(count)