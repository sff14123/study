def solution(l, r):
    answer = []
    q = [5]
    
    while q:
        cur = q.pop(0)
        
        if cur > r:
            continue
            
        if cur >= l:
            answer.append(cur)
            
        q.append(cur * 10)
        q.append(cur * 10 + 5)

    return sorted(answer) if answer else [-1]