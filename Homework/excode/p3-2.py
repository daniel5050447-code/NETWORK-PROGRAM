# 문제 3-2: min_max 함수

def min_max(nums):
    mn = mx = nums[0]
    for n in nums[1:]:
        if n < mn:
            mn = n
        if n > mx:
            mx = n
    return (mn, mx)

nums = list(map(int, input("정수들을 입력하세요: ").split()))
mn, mx = min_max(nums)
print(f"min: {mn}, max: {mx}")
