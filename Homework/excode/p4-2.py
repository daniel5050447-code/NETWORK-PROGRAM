#4-2

filename = input("파일명을 입력하세요: ")
try:
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
except FileNotFoundError:
    print(f"'{filename}' 파일을 찾을 수 없습니다.")
else:
    chars = len(''.join(text.split()))  
    words = len(text.split())
    lines = len(text.splitlines())
    print(f"{'characters':<11}: {chars}")
    print(f"{'words':<11}: {words}")
    print(f"{'lines':<11}: {lines}")
