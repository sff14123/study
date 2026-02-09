students = []
for _ in range(28):
    student = int(input())
    students.append(student)
for i in range(1, 31):
    if not i in students:
        print(i)