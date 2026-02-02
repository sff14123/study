for tc in range(1, 11):
    tc_num, N = map(int, input().split())
    arr = list(map(int, input().split()))
    A = 0 ; B = 99
    graph = [[] for _ in range(101)]
    visited = [False] * 100
    for i in range(N):
        start, end = arr[i*2], arr[i*2+1]
        graph[start].append(end)
    def dfs(n, visited):
        visited[n] = True
        for next in graph[n]:
            if not visited[next]:
                dfs(next, visited)
    dfs(A, visited)
    if visited[B] == True:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)