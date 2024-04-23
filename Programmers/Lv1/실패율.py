def solution(N, stages):
    answer = []
    clear = [0 for _ in range(N + 2)]
    for i in stages:
        clear[i] += 1

    fail_dic = {}
    total = len(stages)

    for i in range(1, N + 1):
        if total == 0:
            fail_dic[i] = 0
        if clear[i] == 0:
            fail_dic[i] = 0
        else:
            fail_dic[i] = clear[i] / total
            total -= clear[i]

    print(fail_dic)

    answer = sorted(fail_dic, key = fail_dic.get, reverse = True)
    # answer = sorted(fail_dic, key=lambda x: fail_dic[x], reverse=True)

    return answer