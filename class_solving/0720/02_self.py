class Person:

    # 사람이라면 이름을 가지고 있다.
    # 인스턴스 생성 시 이름 정보를 받고 싶음
    # 생성자 메서드
    def __init__(self, name):
        # 개별 인스턴스에 각각 name 속성을 지정
        self.name = name

    # self : 호출하는 인스턴스를 파이썬 내부적으로 전달해줌
    # jimin.greeting() 이렇게 호출되면
    # 이런 느낌처럼 작동. Person.greeting(jimin)
    # '내부적으로' 전달. 위 처럼 코드를 쓰지않는다!!!!
    def greeting(self):
        print(f'안녕하세요, {self.name}입니다.')
    # 개별 인스턴스 속성으로 쓰고 싶다
    # 함수에서 어떤 값을 쓰고 싶으면?? 파라미터로 넘겨준다.

# 인스턴스 만들 때
jimin = Person('지민')
jimin.greeting()

iu = Person('지은')
print(iu.name)
iu.greeting()