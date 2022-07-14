# 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
# 모음 : a, e, i, o, u 
# count() 사용 금지
# input : apple / output : 2

word = 'apple'
count = 0
# 지금은 인덱스가 필요없어서
# 그냥 char를 받음
for char in word:
    # if char == 'a' or 'e' or 'i' or 'o' or 'u'
    # 이거 아님
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u': #  혹자는 if - elif 사용
        count += 1
print(count)

count = 0
for char in word:
    # 튜플로 하는 방법
    # ['a', 'e', 'i', 'o', 'u']
    if char in 'aeiou':
        count += 1
print(count)