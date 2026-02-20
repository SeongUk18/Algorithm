import sys

input = sys.stdin.readline

n = int(input())

towers = list(map(int, input().split()))

answer = []
stack = []

for i in range(n):
    cur = towers[i]

    while stack and stack[-1][0] < cur:
        stack.pop()
    
    if stack:
        answer.append(stack[-1][1])
    else:
        answer.append(0)

    stack.append((cur, i + 1))

print(*(answer))