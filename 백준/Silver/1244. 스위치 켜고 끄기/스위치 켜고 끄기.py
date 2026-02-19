switch_n = int(input())
switch = list(map(int,input().split()))
students_n = int(input())
students = [list(map(int,input().split())) for _ in range(students_n)]

for student in students: # 학생들 배열에서 학생 개인을 뽑고
    if student[0] == 1: # 남자면
        for s in range(switch_n): # 스위치 인덱스에서
            if (s+1) % student[1] == 0: # 1-based 기준으로 배수인 수를 반전
                switch[s] = 1 - switch[s]
    else:   # 여자면
        mid = student[1] - 1 # 0-based로 되돌리기
        start = end = mid   # 초기 위치 맞추기
        while 0 < start and end < switch_n - 1:
            if switch[start-1] == switch[end+1]:
                start -= 1
                end += 1
            else:
                break
        for i in range(start, end+1):   # 해당 구간 반전
            switch[i] = 1 - switch[i]
for s in range(0, switch_n, 20):
    print(*switch[s:s+20])