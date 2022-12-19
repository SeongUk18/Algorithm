test_cnt = int(input())
score_list = []
for _ in range(test_cnt):
    score_list.append(list(map(int, input().split())))
# print(score_list)
for score in score_list:
    student_num = score[0]
    average_score = sum(score[1:])/student_num
    cnt = 0
    for i in score[1:]:
        if i > average_score:
            cnt += 1
    rate = cnt / student_num * 100
    print(f'{rate:.3f}%')