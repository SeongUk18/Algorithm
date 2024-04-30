def solution(participant, completion):
    part_dic = {}
    for i in participant:
        if i in part_dic:
            part_dic[i] += 1
        else:
            part_dic[i] = 1
    for i in completion:
        if i in part_dic:
            part_dic[i] -= 1
    # print(part_dic)
    answer = sorted(part_dic, key = part_dic.get, reverse = True)[0]
    # print(answer)
    return answer