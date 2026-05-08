def solution(array):
    cnt = [0] * 1001 
    max_count = 0
    for i in array:
        cnt[i] += 1
        if cnt[i] > max_count:
            max_count = cnt[i]
            
    answer = -1
    count_found = 0
    
    for num in range(len(cnt)):
        if cnt[num] == max_count:
            count_found += 1
            answer = num
            if count_found > 1:
                return -1
                
    return answer