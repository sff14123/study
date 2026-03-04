import sys
n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.read().split()]
for i in range(n):
    for j in range(i, n):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
for i in arr:
    print(i)