a, b = map(int, input().split())
arr = []
i = 1
while len(arr) < b:
    for _ in range(i):
        if len(arr) < b:
            arr.append(i)
        else:
            break
    i += 1
rst = 0
for i in range(a-1, b):
    rst += arr[i]
print(rst)