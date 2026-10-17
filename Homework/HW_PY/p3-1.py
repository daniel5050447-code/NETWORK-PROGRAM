# 문제 3-1: 가변 인수 + 키워드 인수 함수 calc

def calc(*nums, op='+'):
    if op == '+':
        result = 0
        for n in nums:
            result += n
    elif op == '*':
        result = 1
        for n in nums:
            result *= n
    else:
        print("op는 '+' 또는 '*'만 가능합니다")
        return None

    return result

# 테스트
r1 = calc(1, 1, 4, op='+')
print("반환값", r1)
r2 = calc(1, 2, op='*')
print("반환값", r2)
r3 = calc(1, 2, op='-')
print("반환값", r3)
