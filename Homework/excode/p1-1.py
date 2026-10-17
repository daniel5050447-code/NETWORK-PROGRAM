# 연습문제 1-1:입력문

# input() 
a, b = map(int, input("정수 두 개를 입력하세요:").split())
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} x {b} = {a * b}")
print(f"{a} / {b} = {a / b}")

# format() 
a = int(input("첫 번째 정수: "))
b = int(input("두 번째 정수: "))
print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} x {} = {}".format(a, b, a * b))
print("{} / {} = {}".format(a, b, a / b))
