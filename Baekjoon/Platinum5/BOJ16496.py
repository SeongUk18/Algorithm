from functools import cmp_to_key


def compare(x, y):
    if str(x) + str(y) < str(y) + str(x):
        return 1
    elif str(x) + str(y) > str(y) + str(x):
        return -1
    else:
        return 0


n = int(input())

num_list = list(map(int, input().split()))

num_list.sort(key=cmp_to_key(compare))

str = "".join(str(s) for s in num_list)

print(int(str))
