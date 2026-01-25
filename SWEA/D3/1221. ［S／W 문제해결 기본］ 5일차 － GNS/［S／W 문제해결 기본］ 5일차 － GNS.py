T = int(input())
for test_case in range(1, T + 1):
    s = input().split()
    tc_num = s[0]
    N = int(s[1])
    arr = list(input().split())
    num =["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    temp = []
    for i in num:
        for j in range(N):
            if i == arr[j]:
                temp.append(i)
    print(tc_num)
    print(*temp)