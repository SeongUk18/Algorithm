from itertools import permutations
import sys
import heapq

length_list = []
answer_list = []
for _ in range(9):
    length_list.append(int(sys.stdin.readline()))

for i in permutations(length_list, 7):
    if sum(i) == 100:
        answer_list = list(i)
        break

answer_list.sort()
for answer in answer_list:
    print(answer)
