T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    max_v = 0
    for i in range(N):
        for j in range(M):
            s = arr[i][j]
            for n in range(4):
                if 0 <= i + di[n] < N and  0 <= j + dj[n] < M:
                    s += arr[i+di[n]][j+dj[n]]
            if s > max_v:
                max_v = s
    print(f'#{test_case} {max_v}')