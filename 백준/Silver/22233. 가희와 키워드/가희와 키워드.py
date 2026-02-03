from collections import defaultdict
import sys

input=sys.stdin.readline

n, m = map(int, input().split())

words = dict()

for _ in range(n):
    word = input().strip()
    if word not in words:
        words[word] = 0

# print(words)

for _ in range(m):
    memo = list(input().strip().split(','))

    for txt in memo:
        if txt in words:
            del words[txt]
    # print(words)
    print(len(words))
