T = 10

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    total_view = 0

    for i in range(2, N - 2):
        max_arr = arr[i - 2]
        if arr[i - 1] > max_arr:
            max_arr = arr[i - 1]
        if arr[i + 1] > max_arr:
            max_arr = arr[i + 1]
        if arr[i + 2] > max_arr:
            max_arr = arr[i + 2]

        if arr[i] > max_arr:
            total_view += arr[i] - max_arr

    print(f'#{test_case} {total_view}')