n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [False] * (n+1)
tmp = []

def solve(start):

    if len(tmp) == m:
        if not tmp in visited:
            print(' '.join(map(str, tmp)))
            return
    last_n = 0
    for i in range(start, n):
        if not visited[i] and arr[i] != last_n:
            tmp.append(arr[i])
            last_n = arr[i]
            visited[i] = True
            solve(i+1)
            tmp.pop()
            visited[i] = False

solve(0)