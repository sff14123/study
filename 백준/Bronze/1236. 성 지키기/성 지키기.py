N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
r_cnt = 0
c_cnt = 0
for i in range(N):
    if 'X' not in arr[i]:
        r_cnt += 1
for j in range(M):
    for i in range(N):
        if arr[i][j] == 'X':
            break
    else:
        c_cnt += 1
print(max(r_cnt, c_cnt))