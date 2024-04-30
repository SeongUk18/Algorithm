def solution(record):
    answer = []
    command = []
    member_dic = {}
    for i in record:
        if i[0] == "E":
            c, u, n = i.split()
            command.append((c, u))
            member_dic[u] = n
        elif i[0] == "L":
            c, u = i.split()
            command.append((c, u))
        else:
            c, u, n = i.split()
            member_dic[u] = n

    for c, u in command:
        if c[0] == "E":
            answer.append(f"{member_dic[u]}님이 들어왔습니다.")
        else:
            answer.append(f"{member_dic[u]}님이 나갔습니다.")
    return answer