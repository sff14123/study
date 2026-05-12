def solution(x1, x2, x3, x4):
    # answer = (x1 & x2) ^ (x3 & x4)
    answer = True
    ans1 = True
    ans2 = True
    if not (x1 or x2):
        ans1 = False
    if not (x3 or x4) :
        ans2 = False
    if not (ans1 and ans2):
        answer = False
    return answer