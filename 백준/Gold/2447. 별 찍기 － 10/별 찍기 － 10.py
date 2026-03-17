n = int(input())
arr = [[' '] * n for _ in range(n)]
def solve(r, c, n):
    if n == 1:
        arr[r][c] = '*'
        return
    size = n//3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            else:
               solve(r + i*size, c + j*size, size)
solve(0, 0, n)
for r in arr:
    print(''.join(r))