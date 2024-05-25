def solution(array, commands):
    answer = []
    for i in commands:
        start = i[0] - 1
        end = i[1]
        target = i[2]
        # print(i)
        test = array[start:end].copy()
        # print(start, end, target)
        # print(sorted(test))
        answer.append(sorted(test)[target - 1])
    return answer