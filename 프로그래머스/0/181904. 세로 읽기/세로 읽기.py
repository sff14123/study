def solution(my_string, m, c):
    answer = ''
    arr = []
    for i in range(0, len(my_string), m):
        tmp = []
        for j in range(i, i+m):
            tmp.append(my_string[j])
        arr.append(tmp)
    for i in range(len(arr)):
        answer += arr[i][c-1]
        
    return answer