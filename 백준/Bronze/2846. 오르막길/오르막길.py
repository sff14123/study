n = int(input())
arr = list(map(int, input().split()))

tmp = 0
max_v = 0

for i in range(n-1):
    if arr[i] < arr[i+1]:
        tmp += arr[i+1] - arr[i]
        max_v = max(max_v, tmp)
    else:
        tmp = 0
print(max_v)