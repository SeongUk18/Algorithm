from itertools import permutations


def sosu(number):
    if number == 1 or number == 0:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    number_set = set()
    for i in range(1, len(numbers) + 1):
        for j in permutations(numbers, i):
            # print(j)
            number = "".join(j)
            # print(number)
            number = int(number)
            if number not in number_set:
                number_set.add(number)
                if sosu(number):
                    answer += 1

    return answer