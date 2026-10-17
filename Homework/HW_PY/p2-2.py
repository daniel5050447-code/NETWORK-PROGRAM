# 문제 2-2: 딕셔너리


students = {}
while True:
    number = input("학번 입력 (종료: Fin!): ")
    if number == "Fin!":
        break
    name = input("이름 입력: ")
    students[number] = name

print(students)

while True:
    number = input("찾을 학번 입력 (종료: Quit!): ")
    if number == "Quit!":
        print("종료합니다")
        break
    if number in students:
        print(students[number])
    else:
        print("not found!")