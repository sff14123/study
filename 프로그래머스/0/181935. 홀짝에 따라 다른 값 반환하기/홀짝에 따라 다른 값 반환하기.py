def solution(n):
    answer = bool(n%2)
    rst = 0
    if answer:
        for x in range(1,n+1,2):
            rst += x
    else:
        for x in range(2,n+1,2):
            rst += pow(x, 2)
    return rst