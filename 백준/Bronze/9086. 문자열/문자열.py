import sys
t = int(sys.stdin.readline())
for _ in range(t):
    txt = sys.stdin.readline().rstrip()
    print(txt[0]+txt[-1])