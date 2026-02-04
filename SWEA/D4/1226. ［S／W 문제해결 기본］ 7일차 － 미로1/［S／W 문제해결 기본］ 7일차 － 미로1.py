from collections import deque
for tc in range(1, 11):
    tc=int(input())
    maze = [list(input()) for _ in range(16)]
    for y in range(16):
        for x in range(16):
            if maze[y][x] == '2':
                start = (y, x)
                break
            elif maze[y][x] == '3':
                goal = (y, x)
                break
    visited = [[False] * 16 for _ in range(16)]
    q = deque([start])
    visited[start[0]][start[1]] = True
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    found = 0
    while q:
        y, x = q.popleft()
        if maze[y][x] == '3':
            found = 1
            break
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < 16 and 0 <= nx < 16 and maze[ny][nx] != '1' and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx))
    print(f"#{tc} {found}")
