winner = ()
max_score = 0
for i in range(5):
    scores = list(map(int, input().split()))
    if sum(scores) > max_score:
        max_score = sum(scores)
        winner = (i+1, max_score)
print(*winner)