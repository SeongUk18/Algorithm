def solution(want, number, discount):
    answer = 0
    want_dic = {}
    discount_dic = {}
    for i in range(len(want)):
        want_dic[want[i]] = number[i]

    for i in range(len(discount)):
        if discount[i] in discount_dic:
            discount_dic[discount[i]] += 1
        else:
            discount_dic[discount[i]] = 1
        # print(discount_dic)
        if i >= 9:
            # print("w",want_dic)
            # print("d",discount_dic)
            # for j in want:
            #     if j in discount_dic or want_dic[j] != discount_dic[j]:
            #         break
            #     print(i)
            if want_dic == discount_dic:
                answer += 1

            discount_dic[discount[i - 9]] -= 1
            if discount_dic[discount[i - 9]] == 0:
                del discount_dic[discount[i - 9]]

    return answer