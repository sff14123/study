n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
tmp = []
def solve():
    if len(tmp) == m:
        print(' '.join(map(str, tmp)))
        return
    for i in range(n):
        if not arr[i] in tmp:
            tmp.append(arr[i])
            solve()
            tmp.pop()
solve()