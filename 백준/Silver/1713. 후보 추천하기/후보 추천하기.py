n = int(input()) 
total_cnt = int(input())
students = list(map(int, input().split()))

frame = []
time = 0
for student in students:
    time += 1
    found = False
    for i in range(len(frame)):
        if frame[i][0] == student:
            found = True
            frame[i][1] += 1
            break
    if not found:
        if len(frame) >= n:
            frame.sort(key=lambda x: (x[1], x[2]))
            frame.pop(0)
        frame.append([student, 1, time])
rst = []
for f in frame:
    rst.append(f[0])
rst.sort()
for r in rst:
    print(r, end=' ')