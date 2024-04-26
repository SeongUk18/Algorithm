import math


def solution(progresses, speeds):
    answer = []
    time_list = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(len(speeds))]
    print(time_list)
    count = 1
    time = time_list[0]
    for i in time_list[1:]:
        if time >= i:
            count += 1
        else:
            answer.append(count)
            count = 1
            time = i
    answer.append(count)

    return answer