# 문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
# a 가 없는 경우에는 -1을 출력해주세요.
# find() index() 메서드 사용 금지

# 없으면 -1

# Input : banana / Output : 1

# 문자로 순회 하는게 아니라 Index 접근이 포인트
# 1. for-else 풀이
word = 'banana'

# 원하는 숫자? 0, 1, 2, 3, 4, 5
# 얻는 방법은? range(len(word)) => range(6) => 0 ~ 5
for i in range(len(word)):
    # print(i, word[i])
    # 알파벳이 a 일 때
    if word[i] == 'a':
        print(i)
        break
else:
    print(-1)


# a가 있었냐 없었냐 판단? (boolean)
word = 'banana'

# 원하는 숫자? 0, 1, 2, 3, 4, 5
# 얻는 방법은? range(len(word)) => range(6) => 0 ~ 5
is_a = False
for i in range(len(word)):
    if word[i] == 'a':
        print(i)
        i = True
        break

if is_a == False:
# if not is_a: 와 동일
    print(-1)