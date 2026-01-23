T = int(input())
for test_case in range(1, T + 1):
    arr = input()
    change = {'b':'d', 'd':'b', 'p':'q', 'q':'p'}
    arr = [change[i] for i in arr]
    temp = []
    for i in range(len(arr)):
        temp.append(arr[-1-i])
    print(f'#{test_case}', ''.join(temp))