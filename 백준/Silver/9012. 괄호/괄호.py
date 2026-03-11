t = int(input())
for _ in range(t):
    stack = []
    arr = input()
    check = True
    for r in arr:
        if r == '(':
            stack.append(r)
        else:
            if stack:
                stack.pop()
            else:
                print('NO')
                check = False
                break
    if check:
        if stack:
            print('NO')
        else:
            print('YES')