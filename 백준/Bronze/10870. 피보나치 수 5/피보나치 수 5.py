n = int(input())
memo = [0] * 21
def solve(n):
    if n <= 1:
        return n
    if memo[n] != 0:
        return memo[n]
    memo[n] = solve(n - 1) + solve(n - 2)
    return memo[n]
print(solve(n))