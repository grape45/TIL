class Person:
    pass


# Person 클래스의 인스턴스 iu
iu = Person()
# iu의 인스턴스 변수 할당
iu.name = '아이유'
iu.age = 30
iu.gender = 'F'
# 인스턴스 변수 접근
print(iu.name)

# print(iu)
# <__main__.Person object at 0x1060ffca0>
# map과 유사한 결과값이 나옴. map 객체의 특성은 반복 가능한 어떠한 변경된 모습이다.
# 0x1060ffca0 는 메모리 주소를 의미함