remain_set = []
for _ in range(10):
    remain_set.append(int(input()) % 42)
remain_set = set(remain_set)
print(len(remain_set))