N = int(input())
score_list = list(map(int, input().split()))
score = 0
max_score = max(score_list)
for i in score_list:
    new_score = i / max_score * 100
    score += new_score

new_m = score / N
print(new_m)