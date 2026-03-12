from collections import deque
n, k = map(int, input().split())
q = deque([x for x in range(1, n+1)])
rst = []
while q:
    q.rotate(-k+1)
    rst.append(q.popleft())
print('<' + str(rst)[1:-1] + '>')