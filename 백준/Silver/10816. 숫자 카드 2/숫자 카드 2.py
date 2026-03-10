n = int(input())
arr = list(map(int, input().split()))
count = {}
for r in arr:
    if r in count:
        count[r] += 1
    else:
        count[r] = 1
m = int(input())
arr2 = list(map(int, input().split()))
for r in arr2:
    if r in count:
        print(count[r], end=" ")
    else:
        print(0, end=" ")