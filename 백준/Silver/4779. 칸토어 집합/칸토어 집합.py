import sys

def solve(start, length):
    if length == 1:
        return
    piece = length // 3

    for i in range(start + piece, start + piece * 2):
        arr[i] = ' '

    solve(start, piece)
    solve(start + piece * 2, piece)

for line in sys.stdin:
    n = int(line)
    length = 3 ** n
    arr = ['-'] * length
    solve(0, length)
    print(''.join(arr))