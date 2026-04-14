n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
path = [0]
min_value = float('inf')
def solve(current, depth, total_cost):
    global min_value
    if total_cost >= min_value:
        return
    if depth == n:
        return_cost = arr[current][0]
        if return_cost > 0:
            min_value = min(min_value, total_cost + return_cost)
        return
    for i in range(n):
        if not i in path and arr[current][i] > 0:
            path.append(i)
            solve(i, depth + 1, total_cost + arr[current][i])
            path.pop()
solve(0, 1, 0)
print(min_value)