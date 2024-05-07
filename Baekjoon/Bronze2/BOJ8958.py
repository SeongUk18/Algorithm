trial_num = int(input())
result_score = []
for _ in range(trial_num):
    result_score.append(input())
for result in result_score:
    score = 0
    cnt = 0
    for O_X in range(len(result)):
        if result[O_X] == "O":
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)