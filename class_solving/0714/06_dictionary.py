# 기본 순회
# key가 기준이고, 직접 딕셔너리에 key로 접근하면 value를 얻을 수 있다 !
my_dict = {'apple' : '사과', 'banana' : '바나나'}

for word in my_dict:
    print(word)
# apple
# banana
# key 값을 출력한다.

# value 값 접근?
    print(word, my_dict[word])
# apple 사과
# banana 바나나

# 심화 형태
# 다양한 방법 -> 일종의 리스트!
# print(my_dict.key())
print(my_dict.key(), type(my_dict.keys()))
# dict_keys(['apple', 'banana'])
print(my_dict.value())
# dict_values(['사과', '바나나'])
for value in my_dict.values():
    print(value)


print(my_dict.items())
for k, v in my_dict.items():
    print(k, v)
# 일종의 리스트안에, tuple!
# dict_items([('apple', '사과'), ('banana', '바나나')])


# dictionary에 값 추가 방법
my_dict_2 = {}
my_dict_2['a'] = 'airplane'

my_dict_3 = {'a' : 0}
my_dict_3['a'] += 1
# my_dict_3 = my_dict_3['a'] + 1 과 동일 코드
print(my_dict_3)
# {'a' : 1}

my_list = [0, 1, 2]
my_list[0] - my_list[0] + 1

# 리스트와 딕셔너리
[1, 2, 3] + [4, 5]
# [1, 2, 3, 4, 5]

{'a' : 'apple'} + {'b' : 'banana'}
# Error
# dictionaryd는 더할 수 없다.