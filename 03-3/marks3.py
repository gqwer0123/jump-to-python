marks = [90, 25, 67, 45, 80]

for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print(f'{number+1}번 학생 축하합니다. 합격입니다.')