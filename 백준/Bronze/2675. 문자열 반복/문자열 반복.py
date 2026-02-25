import sys
t = int(sys.stdin.readline())
for _ in range(t):
    r, s = sys.stdin.readline().split()
    result = "".join([i * int(r) for i in s])
    print(result)