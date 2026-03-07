import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
count = 1

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i].sort(reverse=True)

def dfs_iterative(start_node):
    global count
    stack = [start_node]
    
    while stack:
        curr = stack.pop()
        
        if visited[curr] == 0:
            visited[curr] = count
            count += 1
            
            for next_node in graph[curr]:
                if visited[next_node] == 0:
                    stack.append(next_node)

dfs_iterative(r)

sys.stdout.write('\n'.join(map(str, visited[1:])) + '\n')