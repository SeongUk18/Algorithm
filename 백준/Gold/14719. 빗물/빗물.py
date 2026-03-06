import sys

input = sys.stdin.readline

h, w = map(int, input().split())

col_list = list(map(int, input().split()))

left_max = [0] * w
right_max = [0] * w

left_max[0] = col_list[0]
for i in range(1, w):
    left_max[i] = max(left_max[i - 1], col_list[i])

right_max[-1] = col_list[-1]
for i in range(w - 2, -1, -1):
    right_max[i] = max(right_max[i + 1], col_list[i])

answer = 0
for i in range(w):
    water = min(left_max[i], right_max[i]) - col_list[i]

    if water > 0:
        answer += water

print(answer)