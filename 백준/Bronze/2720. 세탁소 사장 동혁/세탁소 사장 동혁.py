import sys
t = int(sys.stdin.readline())
for _ in range(t):
    c = int(sys.stdin.readline())
    q = c // 25
    d = c % 25 // 10
    e = c % 25 % 10 // 5
    p = c % 25 % 10 % 5
    print(q, d, e, p)