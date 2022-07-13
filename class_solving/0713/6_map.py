numbers = ['1', '2', '3']

# 숫자로 바꿔서 쓰고 싶다?
# 리스트를 숫자로 형 변환은 불가능
# 다만, 숫자 형태의 문자를 변환할 수는 있다.
# n = int(numbers)

# 이렇게 가능함, 근데 100개, 1000개 인 경우엔?
a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])
new_numbers = [a, b, c]

# 반복문
print(numbers)
new_numbers = []
for number in numbers:
    new_numbers.append(int(number))
print(new_numbers)

# map !
numbers = ['1', '2', '3']
new_numbers_2 = map(int, numbers)
print(new_numbers_2, type(new_numbers_2)) 
# <map object at 0x104369be0> : 이미 함수가 모두 적
# <class 'map'>
print(list(new_numbers_2)) 
# 리스트로 형변환해서 보면 바뀌어있다.
# 확인하기 위해 리스트로 바꾼 것임, 반드시 List로 바꿀 필요 없다.