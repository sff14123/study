T = int(input())
for test_case in range(1, T + 1):
    arr = input()
    for i in range(len(arr)):
        cnt = 0
        if arr[i] == arr[-1-i]:
            cnt = 1
    print(f'#{test_case} {cnt}')