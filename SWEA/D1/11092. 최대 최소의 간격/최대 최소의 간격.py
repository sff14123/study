T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_num = 1
    min_num = 10
    max_idx = 4
    min_idx = 99
    for i in range(N):
        if arr[i] >= max_num:
            max_num = arr[i]
            max_idx = i
    for i in range(N):
        if arr[i] < min_num:
            min_num = arr[i]
            min_idx = i
        result = max_idx - min_idx
        if result < 0:
            result = - result
    print(f'#{test_case} {result}')