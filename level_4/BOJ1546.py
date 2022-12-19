subject_count = int(input())
subject_score = []
sum_score = 0
subject_score = list(map(int, input().split()))
max_score = max(subject_score)
for i in range(subject_count):
    sum_score += subject_score[i]/max_score*100
average_score = sum_score/subject_count
print(average_score)