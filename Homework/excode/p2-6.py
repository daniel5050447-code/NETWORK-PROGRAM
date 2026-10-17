# 문제 2-6: 소수 찾기

n = int(input("1~100 사이의 자연수를 입력하세요: "))

if n < 1 or n > 100:
    print("1에서 100 사이의 자연수를 입력하세요.")
elif n == 1:
    print("1은 소수가 아닙니다")
else:
    for d in range(2, n):
        if n % d == 0:
            print(f"{n}은 소수가 아닙니다")
            break
    else:                      
        print(f"{n}은 소수입니다")
