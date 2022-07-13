# sep에 대한 이해

print('hello', 'hi') # helllo hi
print('hello', 'hi', sep='-') # hello-hi
# 기본값이 sep는 ' ' 으로 정의가 되어 있음.
# 키워드로 sep을 바꿔서 호출할 수 있음
print(1, 2, 3, 4, 5, 6, 7, 8)

# 정해지지 않은 갯수의 인자
def my_add(*numbers):
  # 내부적으로 numbers가 tuple
  return numbers

result = my_add(1, 2, 3)
print(result, type(result)) # (1, 2, 3) <class 'tuple'>

def my_func(**kwargs):
  return kwargs

result = my_func(name = '홍길동', age = '100', gender = 'M') 
# key-value 를 쌍으로 넘겨줌, Dictionary
# {name = '홍길동', age = '100', gender = 'M'} --- 확인 필요
print(result, type(result))