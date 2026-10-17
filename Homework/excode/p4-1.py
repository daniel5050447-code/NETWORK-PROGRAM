# 4-1
while True:
    filename = input("파일명을 입력하세요 (종료: q): ")
    if filename == 'q':
        print("종료합니다.")
        break
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"'{filename}' 파일이 없습니다. 다시 입력하세요.")
        continue

    numbered = [f"{i} {line.rstrip()}" for i, line in enumerate(lines, 1)]
    for line in numbered:
        print(line)

    savename = filename.rsplit('.', 1)[0] + '.sav'
    with open(savename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(numbered) + '\n')
    print(f"'{savename}' 파일로 저장")
    break
