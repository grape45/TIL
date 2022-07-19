class Person:

    # 생성자! 인스턴스가 생성될 때 어떠한 작업을 하기 위함!
    def __init__(self, name):
        # 그 인스턴스의 이름을 name으로 해주세요.
        self.name = name

# Person 클래스의 인스턴스인 iu를 생성
iu = Person('아이유')
print(iu.name)
jimin = Person('지민')
print(jimin.name)