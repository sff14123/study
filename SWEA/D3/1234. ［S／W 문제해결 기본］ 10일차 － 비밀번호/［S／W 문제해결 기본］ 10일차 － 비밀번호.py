def push(i):
    global top
    if top >= N - 1:
        return
    top += 1
    stack[top] = i

def pop():
    global top
    if top == -1:
        return
    stack[top] = 0
    top -= 1

T = 10
for tc in range(1, T+1):
    N, arr = input().split()
    N = int(N)
    arr = list(arr)
    top = -1
    stack = [0] * N
    for i in range(N):
        push(arr[i])
        if top > 0 and stack[top] == stack[top - 1]:
            pop()
            pop()

    print(f'#{tc}', end=' ')
    for i in range(top + 1):
        print(stack[i], end='')
    print()