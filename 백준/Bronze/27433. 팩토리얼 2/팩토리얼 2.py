import sys
input = lambda : sys.stdin.readline()
n = int(input())
def solve(n):
    if n < 2:
        return 1
    return n * solve(n-1)
print(solve(n))