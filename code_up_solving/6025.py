# 입력받은 숫자에 5를 더한 결과를 출력하세요.
num = input()
# input은 모두 string으로 저장됩니다. 아무리 숫자 형태라고 해도요.
# print(num + 5) 가 아니라,
print(int(num) + 5)
# 숫자로 활용하기 위해 int로 변환 !