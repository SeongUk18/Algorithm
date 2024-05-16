def solution(enroll, referral, seller, amount):
    answer = []
    parent = dict(zip(enroll, referral))
    # print(parent)
    total = {name: 0 for name in enroll}
    # print(total)

    for i in range(len(seller)):
        money = amount[i] * 100
        cur_name = seller[i]

        while money > 0 and cur_name != "-":
            total[cur_name] += money - money // 10
            cur_name = parent[cur_name]
            money //= 10
    # print(total)
    answer = [total[name] for name in enroll]
    return answer

# numbers = [1, 2, 3]
# letters = ["A", "B", "C"]
# for pair in zip(numbers, letters):
#     print(pair)
# (1, 'A')
# (2, 'B')
# (3, 'C')