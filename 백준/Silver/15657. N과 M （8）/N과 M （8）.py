n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
tmp = []
def solve(start):
    if len(tmp) == m:
        print(' '.join(map(str, tmp)))
        return
    for i in range(start, n):
        tmp.append(arr[i])
        solve(i)
        tmp.pop()
solve(0)