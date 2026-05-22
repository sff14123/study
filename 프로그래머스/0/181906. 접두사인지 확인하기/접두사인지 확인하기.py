def solution(my_string, is_prefix):
    answer = 0
    str_arr = []
    for idx in range(len(my_string)):
        str_arr.append(my_string[:idx+1])
    if is_prefix in str_arr:
        answer = 1
    return answer