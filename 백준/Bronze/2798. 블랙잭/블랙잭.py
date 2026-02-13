n, m = map(int, input().split())
arr = list(map(int, input().split()))
max_v = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            tmp = arr[i]+arr[j]+arr[k]
            if m >= tmp:
                max_v = max(max_v, tmp)
print(max_v)
