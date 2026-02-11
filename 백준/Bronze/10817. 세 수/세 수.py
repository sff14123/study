A, B, C = map(int, input().split())
arr = [A, B, C]
for i in range(2, -1, -1):
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr[1])