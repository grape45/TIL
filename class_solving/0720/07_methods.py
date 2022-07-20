# 함수 내부에서 값을 쓰고 싶으면 어떻게 해야하죠?
# 정의할 때 이름을 지어놓고, 호출할 때 값을 넘겨줘요 !

class MyClass:
    class_variable = '클래스변수'

    # 메서드들을 정의했습니다.
    def __init__(self):
        self.instance_variable = '인스턴스 변수'

    # 인스턴스 메서드 정의
    def instance_method(self):
        return self, self.instance_variable
        # 인스턴스 메서드 호출 (<__main__.MyClass object at 0x101447070>, '인스턴스 변수')
    
    # 클래스 메서드 정의
    @classmethod
    # @ : 데코레이터, 함수를 꾸며주는 역할, 장고에서 활용 예정
    def class_method(cls):
        return cls, cls.class_variable
        # 클래스 메서드 호출 (<class '__main__.MyClass'>, '클래스변수')
    
    # 스태틱 메서드 정의
    @staticmethod
    def static_method():
        return ''
        # 스태틱 메서드 호출 

c1 = MyClass()
print('인스턴스 변수 호출', c1.instance_variable)
print('인스턴스 메서드 호출', c1.instance_method())
print('클래스 메서드 호출', c1.class_method())
print('스태틱 메서드 호출', c1.static_method())