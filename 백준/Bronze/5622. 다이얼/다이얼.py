import sys
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
txt = sys.stdin.readline().rstrip()
time = 0
for t in txt:
    for i, d in enumerate(dial):
        if t in d:
            time += i+3
            break
print(time)