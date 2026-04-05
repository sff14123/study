t = int(input())
for _ in range(t):
    arr = input()
    solve = 0
    tmp = 1
    for r in arr:
        if r == 'O':
            solve += tmp
            tmp += 1
        else:
            tmp = 1
    print(solve)