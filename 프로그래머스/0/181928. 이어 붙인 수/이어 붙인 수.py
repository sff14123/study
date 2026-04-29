def solution(num_list):
    e = ''
    o = ''
    for num in num_list:
        if num % 2 == 0:
            e += str(num)
        else:
            o += str(num)
    answer = int(e) + int(o)    
    
    return answer