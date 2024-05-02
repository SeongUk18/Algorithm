def solution(id_list, report, k):
    answer = []
    id_dic = {i : [] for i in id_list}
    report_dic = {i : 0 for i in id_list}
    for r in report:
        a, b = r.split()
        if b not in id_dic[a]:
            id_dic[a].append(b)
            report_dic[b] += 1
    # print(id_dic)
    # print(report_dic)
    for key, vals in id_dic.items():
        count = 0
        for v in vals:
            # print(v)
            if report_dic[v] >= k:
                count += 1
        answer.append(count)
    return answer