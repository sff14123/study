import sys

n, k = map(int, sys.stdin.readline().split())

factors = []

for i in range(1, n + 1):
    if n % i == 0:
        factors.append(i)

if len(factors) >= k:
    print(factors[k-1])
else:
    print(0)