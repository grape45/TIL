def foo():
    return 1, 2

result = foo()
print(result, type(result)) # (1, 2) <class 'tuple'>

def no():
    a = 1

result = no()
print(result, type(result)) # None <class 'NoneType'>


# print 함수는
# 출력을 해주고, return 값은 없다. (None)
a = print('hi') # 잘못 작성한 코드
print(a, type(a)) # None <class 'NoneType'>

a = 'hi'
print(a) # 위의 코드를 작성한 기저는 이 코드를 작성하고 싶었을 거다.