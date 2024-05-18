from collections import Counter
from itertools import combinations


def solution(orders, course):
    answer = []
    for c in course:
        menu = []
        for order in orders:
            com = combinations(sorted(order), c)
            menu += com
        # print(menu)
        counter = Counter(menu)
        # print(counter)
        if len(counter) != 0 and max(counter.values()) != 1:
            for m, cnt in counter.items():
                # print(m, cnt)
                if cnt == max(counter.values()):
                    answer.append("".join(m))

    return sorted(answer)

# c = Counter('hello')
# print(c)  # 결과: Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})