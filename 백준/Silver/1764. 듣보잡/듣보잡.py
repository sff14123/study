n, m = map(int, input().split())
arr = {input() for _ in range(n)}
arr2 = {input() for _ in range(m)}
rst = list(arr & arr2)
rst.sort()
print(len(rst))
for r in rst:
    print(r)