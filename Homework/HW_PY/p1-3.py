# 연습문제 1-3: 수식계산
import math

# 1-3-1
a, b, c = 3, 4, 5
print("(1)", 1 / (1 + a / b + c))

# 1-3-2
a, b, c = 1, 1, -6
d = b ** 2 - 4 * a * c
x1 = (-b + math.sqrt(d)) / (2 * a)
x2 = (-b - math.sqrt(d)) / (2 * a)
print("(2)", x1, x2)

# 1-3-3
r = 5
print("(3)", math.pi * r ** 2)

# 1-3-4
b, g = 2.0, 3.2
print("(4)", b * math.exp(-g))

# 1-3-5
x, m, rh = 0, 1.5, 2.0
print("(5)", 1 / math.sqrt(2 * math.pi * rh) * math.exp((x - m) ** 2 / (2 * rh ** 2)))
