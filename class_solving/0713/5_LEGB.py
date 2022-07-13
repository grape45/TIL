# LEGB
sum = 5

print(sum([1, 2, 3]))

# Traceback (most recent call last):
#  File "/Users/jodeoggyu/Desktop/TIL/class_solving/0713/function_5.py", line 4, in <module>
#    print(sum([1, 2, 3]))
# TypeError: 'int' object is not callable

# sum이 지금은 5가 되어버림 T.T
# Built-in scope에 sum 함수가 있었음.
# Global scope에 sum 이름의 변수를 만들었음.
# 제가 찾았으니까 L -> E -> G -> B