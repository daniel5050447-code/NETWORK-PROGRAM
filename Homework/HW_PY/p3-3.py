# 문제 3-3: count_vowel 함수

def count_vowel(s):
    count = 0
    for ch in s.lower():
        if ch in 'aeiou':
            count += 1
    return count

text = input("문자열을 입력하세요: ")
print(f"모음의 개수: {count_vowel(text)}")
