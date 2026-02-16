import sys
def check_bingo(board):
    line_count = 0
    for row in board:
        if sum(row) == 0:
            line_count += 1
    for c in range(5):
        if sum(board[r][c] for r in range(5)) == 0:
            line_count += 1
    if sum(board[i][i] for i in range(5)) == 0:
        line_count += 1
    if sum(board[i][4 - i] for i in range(5)) == 0:
        line_count += 1

    return line_count

my_board = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
numbers = []
for _ in range(5):
    numbers.extend(list(map(int, sys.stdin.readline().split())))

pos = {}
for r in range(5):
    for c in range(5):
        pos[my_board[r][c]] = (r, c)

for i in range(len(numbers)):
    num = numbers[i]
    r, c = pos[num]
    my_board[r][c] = 0 

    if check_bingo(my_board) >= 3:
        print(i + 1)
        break