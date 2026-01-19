T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    cnt = 1
    k = 0

    while cnt <= N**2:

            for i in range(k, N - k):
                arr[k][i] = cnt
                cnt += 1

            for i in range(k + 1, N - k):
                arr[i][N - 1 - k] = cnt
                cnt += 1

            for i in range(N - 2 - k, k - 1, - 1):
                arr[N - 1 - k][i] = cnt
                cnt += 1

            for i in range(N - 2 - k, k, -1):
                arr[i][k] = cnt
                cnt += 1

            k += 1

    print(f'#{test_case}')
    for row in arr:
        print(*row)