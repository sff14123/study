import sys

def solve(start, depth):
    if depth == 6:
        print(*ans)
        return

    for i in range(start, k):
        ans.append(s[i])
        solve(i + 1, depth + 1)
        ans.pop()

while True:
    line = list(map(int, sys.stdin.readline().split()))
    if line[0] == 0:
        break
    
    k = line[0]
    s = line[1:]
    ans = []
    
    solve(0, 0)
    print()