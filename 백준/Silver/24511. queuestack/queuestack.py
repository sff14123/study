from collections import deque
n = int(input())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))
m = int(input())
arr_c = list(map(int, input().split()))
q = deque()
for i in range(n):
    if arr_a[i] == 0:
        q.append(arr_b[i])
for c in arr_c:
    if q:
        q.appendleft(c)
        print(q.pop(), end = ' ')
    else:
        print(c, end = ' ')