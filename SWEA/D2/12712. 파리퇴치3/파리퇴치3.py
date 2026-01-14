T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    dx = [-1, 1, -1, 1]
    dy = [-1, -1, 1, 1]
    max_k = 0
    for i in range(N):
        for j in range(N):
            s = arr[i][j]
            s2 = arr[i][j]
            for m in range(1, M):
                for n in range(4):
                    ni = i + di[n]*m
                    nj = j + dj[n]*m
                    if 0 <= ni < N and 0 <= nj < N:
                        s += arr[ni][nj]
                    nx = i + dx[n] * m
                    ny = j + dy[n] * m
                    if 0 <= nx < N and 0 <= ny < N:
                        s2 += arr[nx][ny]
            if s > max_k:
                max_k = s
            if s2 > max_k:
                max_k = s2
    print(f'#{test_case} {max_k}')