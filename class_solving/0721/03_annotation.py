# 동적 타입 언어인 파이썬에서
# 정적 타입으로 바꿔 주는 것이 아니다!!
# 그냥 힌트... 그냥 노트를 위한 것

# 변수 어노테이션
a: int = 3
print(a)

# 함수 어노테이션
# 아래 x, y를 int로 주는건 가이드(힌트)) 정도에 불과. 꼭 int를 써야하는건 아님 
def add(x : int, y : int) -> int:
    return x + y

print(add(7, 4))
print(add('hi ', 'hello'))

# 함수 어노테이션
def add2(x, y):
    return x + y
print(add2(7, 4))