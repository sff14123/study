T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if A[i] != B[i]:
            cnt += 1
            for j in range(i, N):
                A[j] = 1 - A[j]
    print(f'#{test_case} {cnt}')