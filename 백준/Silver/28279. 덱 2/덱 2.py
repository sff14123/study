from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()
n = int(input())
q = deque()
for _ in range(n):
    line = list(map(int, input().split()))
    if line[0] == 1:
        q.appendleft(line[1])
    elif line[0] == 2:
        q.append(line[1])
    elif line[0] == 3:
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif line[0] == 4:
        if q:
            print(q.pop())
        else:
            print(-1)
    elif line[0] == 5:
        print(len(q))
    elif line[0] == 6:
        if not q:
            print(1)
        else:
            print(0)
    elif line[0] == 7:
        if q:
            print(q[0])
        else:
            print(-1)
    elif line[0] == 8:
        if q:
            print(q[-1])
        else:
            print(-1)