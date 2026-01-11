T = int(input())
 
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
 
    for i in range(N):
        for j in range(N - i):
            if arr[i] > arr[i + j]:
                arr[i], arr[i + j] = arr[i + j], arr[i]
 
    print(f'#{test_case} {" ".join(map(str, arr))}')