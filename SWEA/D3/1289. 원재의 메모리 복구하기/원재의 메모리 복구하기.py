T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(int, input()))
    now = 0
    cnt = 0
    for i in range(len(arr)):
        if arr[i] != now:
            cnt += 1
            now = arr[i]
    print(f'#{test_case} {cnt}')