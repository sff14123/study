from collections import deque
n = int(input())
q = deque([x for x in range(1,n+1)])
end = 0
while q:
    end = q.popleft()
    if q:
        q.append(q.popleft())
print(end)