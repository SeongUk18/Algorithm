from functools import cmp_to_key


def compare(x, y):
    if str(x) + str(y) > str(y) + str(x):
        return - 1
    elif str(x) + str(y) == str(y) + str(x):
        return 0
    elif str(x) + str(y) < str(y) + str(x):
        return 1


def solution(numbers):
    answer = ''
    # numbers = list(' '.join(str(s) for s in numbers).split())
    # print(numbers)
    numbers = sorted(numbers, key = cmp_to_key(compare))
    for n in numbers:
        answer += str(n)
    return answer if answer.strip('0') != '' else '0'