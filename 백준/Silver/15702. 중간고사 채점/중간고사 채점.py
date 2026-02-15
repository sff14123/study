N, M = map(int, input().split())
scores = [0] + list(map(int, input().split()))
first = ["", -1]
for _ in range(M):
    line = input().split()
    student_id = line[0]
    results = line[1:]  
    current_score = 0
    for j in range(N):
        if results[j] == 'O':
            current_score += scores[j + 1]
    if current_score > first[1]:
        first = [student_id, current_score]
    elif current_score == first[1]:
        if int(student_id) < int(first[0]):
            first = [student_id, current_score]
print(first[0], first[1])