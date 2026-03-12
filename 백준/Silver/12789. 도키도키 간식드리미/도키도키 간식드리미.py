n = int(input())
arr = list(map(int, input().split()))
stack = []
cur = 1
for a in arr:
    stack.append(a)
    while stack and stack[-1] == cur:
        stack.pop()
        cur += 1
if not stack:
    print('Nice')
else:
    print('Sad')