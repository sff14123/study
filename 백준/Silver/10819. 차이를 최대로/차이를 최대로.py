n = int(input())
nums = list(map(int, input().split()))

visited = [False] * n
temp = []  
max_val = 0

def solve(depth):
    global max_val

    if depth == n:
        current_sum = 0
        for i in range(n - 1):
            current_sum += abs(temp[i] - temp[i + 1])

        max_val = max(max_val, current_sum)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            temp.append(nums[i])  
            solve(depth + 1) 
            temp.pop()
            visited[i] = False

solve(0)
print(max_val)