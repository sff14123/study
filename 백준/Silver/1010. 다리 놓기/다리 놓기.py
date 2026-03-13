def solve(i, j):
    if j == 0 or i == j:
        return 1
    if memo[i][j] != 0:
        return memo[i][j]
    memo[i][j] = solve(i-1, j-1) + solve(i-1, j)
    return memo[i][j]
t = int(input())
memo = [[0] * 31 for _ in range(31)]
for _ in range(t):
    n, m = map(int, input().split())
    print(solve(m, n))