def solution(answers):
    answer = []
    p_1 = [1, 2, 3, 4, 5]
    p_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    p_score = [0] * 3
    for i in range(len(answers)):
        if answers[i] == p_1[i % len(p_1)]:
            p_score[0] += 1
        if answers[i] == p_2[i % len(p_2)]:
            p_score[1] += 1
        if answers[i] == p_3[i % len(p_3)]:
            p_score[2] += 1
    max_score = max(p_score)
    print(p_score.index(max_score))
    for i in range(len(p_score)):
        if p_score[i] == max_score:
            answer.append(i + 1)

    return answer