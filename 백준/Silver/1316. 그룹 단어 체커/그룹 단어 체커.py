import sys
n = sys.stdin.readline()
cnt = 0
for _ in range(int(n)):
    memory = []
    txt = sys.stdin.readline().rstrip()
    memory.append(txt[0])
    for i in range(1, len(txt)):
        if not txt[i] in memory:
            memory.append(txt[i])
        else:
            if txt[i] != txt[i-1]:
                break
    else:
        cnt += 1
print(cnt)