word = 'banana'

# 1차적인 단순한 생각
# print(word)
cnt_a = 0
cnt_b = 0
cnt_c = 0
cnt_d = 0
cnt_e = 0
cnt_f = 0
cnt_g = 0
cnt_h = 0
cnt_i = 0
cnt_j = 0
cnt_k = 0

for i in word:
    if i == 'a':
        cnt_a += 1
    elif i == 'b':
        cnt_c += 1
    elif i == 'c':
        cnt_b += 1
    elif i == 'd':
        cnt_d += 1


# 데이터를 기록 => Key와 Value => 딕셔너리
# strawberry, blueberry => 값들의 나열 => 리스트


# 2차 풀이
word = 'banana'

# print(word)
result = {}

# 문자열을 반복하면서 알파벳 하나씩이 char
for char in word:
    print(char)
    # 만약에 기존에 키가 없으면, 1로 초기화를 하고
    if char in result:
        result[char] = 1
    # 키가 있으면, 기존 값에 더하자!
    else:
        result[char] = result[char] + 1


print(result)

# (참고) 딕셔너리에서 키-값의 쌍 추가
# result = {}
# result['a'] = 0
# print(result)

# # (참고)리스트에서 값의 추가 방법
# my_list = []
# my_list.append(1) 
# # 리스트의 값 추가는 .append()로 해야함
# print(my_list)
