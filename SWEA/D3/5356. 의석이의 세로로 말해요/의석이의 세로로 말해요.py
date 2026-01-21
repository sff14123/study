T = int(input())
for test_case in range(1, T + 1):
    arr = [list(input()) for _ in range(5)]
    col_lst = []
    for i in range(15):
        for j in range(5):
            if i < len(arr[j]):
                col_lst.append(arr[j][i])
    print(f'#{test_case}', ''.join(col_lst))