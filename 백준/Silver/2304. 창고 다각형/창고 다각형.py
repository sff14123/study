n = int(input())
arr = []
rst = 0
for _ in range(n):
    l, h = map(int, input().split())
    arr.append([l, h])
arr.sort()

max_h = 0
max_idx = 0
for i in range(n):
    if arr[i][1] > max_h:
        max_h = arr[i][1]
        max_idx = i

rst = 0

curr_h = 0
for i in range(max_idx):
    curr_h = max(curr_h, arr[i][1])
    rst += curr_h * (arr[i+1][0] - arr[i][0])

curr_h = 0
for i in range(len(arr)-1, max_idx, -1):
    curr_h = max(curr_h, arr[i][1])
    rst += curr_h * (arr[i][0] - arr[i-1][0])

rst += max_h
print(rst)