T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_k = 0
    for n in range(N):
        for m in range(N):
            if n + M <= N and m + M <= N:
                s = 0
                for i in range(n, n+M):
                    for j in range(m, m+M):
                        s += arr[i][j]
                    if max_k < s:
                        max_k = s
    print(f'#{test_case} {max_k}')