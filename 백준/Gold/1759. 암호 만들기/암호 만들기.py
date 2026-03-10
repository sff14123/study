l, c = map(int, input().split())
arr = list(input().split())
arr.sort()
def solve(start, depth):
    cnt = ['a', 'e', 'i', 'o', 'u']
    cnt1 = 0
    cnt2 = 0
    if depth == l:
        for r in rst:
            if r in cnt:
                cnt1 += 1
            else:
                cnt2 += 1
        if cnt1 > 0 and cnt2 > 1:
            print(''.join(map(str, rst)))
            return
    for i in range(start, c):
        rst.append(arr[i])
        solve(i+1, depth+1)
        rst.pop()
rst = []
solve(0, 0)