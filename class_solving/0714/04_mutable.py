# 리스트는 mutable
a = [1, 2, 3]
a[0] = 100
print(a)
# [100, 2, 3]

# 문자열은 immutable
a = 'hi'
a[0] = 'c'
print(a)
# 오류 발생
# 'str' object does not support item assignment


# 변경 가능 / 변경 불가능을 구분하는 방법임. 리스트, 문자열 그 자체의 특성에 비롯됨
# 따라서 문자열은 첫 번째 인덱스에 해당하는 값을 바꿀 수 '없다'
# 리스트는 바꿀 수 '있다'

# 인덱스에 접근하는 것과 바꾸는 건 또 다른 문제임