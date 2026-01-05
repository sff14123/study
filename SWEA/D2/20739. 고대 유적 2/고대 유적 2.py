T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0
    for i in range(N):
        r_cnt = 0
        for j in range(M):
            if arr[i][j] == 1:
                r_cnt += 1
                if r_cnt > max_cnt:
                    max_cnt = r_cnt
            else:
                r_cnt = 0
    for i in range(M):
        c_cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                c_cnt += 1
                if c_cnt > max_cnt:
                    max_cnt = c_cnt
            else:
                c_cnt = 0
    if max_cnt == 1:
        max_cnt = 0
    print(f'#{tc}', max_cnt)