n = int(input())
arr = []
visited = [False] * (n + 1)
def solve(depth):
    if depth == n:
        print(*arr)
        return
    for i in range(1, n+1):
        if not visited[i]:
            arr.append(i)
            visited[i] = True
            solve(depth + 1)
            arr.pop()
            visited[i] = False
solve(0)