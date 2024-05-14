def solution(clothes):
    answer = 1

    cloth_dic = {}
    for i in clothes:
        types = i[1]
        if types in cloth_dic:
            cloth_dic[types] += 1
        else:
            cloth_dic[types] = 1

    # print(cloth_dic)
    for val in cloth_dic.values():
        answer *= val + 1

    return answer - 1