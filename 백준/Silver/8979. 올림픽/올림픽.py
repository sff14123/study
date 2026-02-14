n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n - 1 - i):
        if arr[j][1] < arr[j+1][1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
        elif arr[j][1] == arr[j+1][1]:
            if arr[j][2] < arr[j+1][2]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            elif arr[j][2] == arr[j+1][2]:
                if arr[j][3] < arr[j+1][3]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

target_idx = 0
for i in range(n):
    if arr[i][0] == k:
        target_idx = i
        break

for i in range(n):
    if arr[i][1:4] == arr[target_idx][1:4]:
        print(i + 1)
        break