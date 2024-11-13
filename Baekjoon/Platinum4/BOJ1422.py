from functools import cmp_to_key


def compare(x, y):
    if str(x) + str(y) > str(y) + str(x):
        return -1
    elif str(y) + str(x) > str(x) + str(y):
        return 1
    else:
        return 0


n, k = map(int, input().split())

num_list = []

for _ in range(n):
    num_list.append(int(input()))

for _ in range(k - n):
    num_list.append(max(num_list))

# print(num_list)
num_list.sort(key=cmp_to_key(compare))

print(*num_list, sep="")
