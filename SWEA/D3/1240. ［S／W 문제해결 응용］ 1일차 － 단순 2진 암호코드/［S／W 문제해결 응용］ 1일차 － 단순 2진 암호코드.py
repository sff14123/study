T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    pw = {'0001101':'0', '0011001':'1', '0010011':'2', '0111101':'3','0100011':'4', '0110001':'5',
          '0101111':'6', '0111011':'7', '0110111':'8', '0001011':'9'}
    scan = [0] * M
    start = 0
    code = [0] * 56
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '1':
                start = i
            scan[j] = arr[start][j]

    while scan[-1] == '0':
        scan.pop()

    stack = [0] * 56
    top = -1
    for l in range(len(scan)-1, -1, -1):
        if top < 55:
            top += 1
            stack[top] = scan[l]


    for i in range(56):
        code[i] = stack[top]
        top -= 1
    password = []
    for i in range(0, 56, 7):
        password.append(code[i:i+7])
    word = [''.join(i) for i in password]
    result = []
    for i in word:
        if i in pw:
            i = pw[i]
            result.append(int(i))
    s1 = 0 # 홀수자리
    s2 = 0 # 짝수자리
    
    for i in range(4):
        s1 += result[i*2]
        s2 += result[i*2+1]
    if (s1*3+s2) % 10 == 0:
        print(f'#{tc}', s1+s2)
    else:
        print(f'#{tc}', 0)