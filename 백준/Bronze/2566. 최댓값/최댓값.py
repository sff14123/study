import sys
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
max_v = -1
max_idx = ()
for i in range(9):
    for j in range(9):
        if arr[i][j] > max_v:
            max_v = arr[i][j]
            max_idx = i+1, j+1
print(max_v)
print(*max_idx)