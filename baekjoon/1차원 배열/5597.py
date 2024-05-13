homework = []

for i in range(28):
    student = int(input())
    homework.append(student)

for i in range(1, 31):
    if i not in homework:
        print(i)