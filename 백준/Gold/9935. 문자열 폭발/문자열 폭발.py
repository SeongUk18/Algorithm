import sys

input = sys.stdin.readline

st = input().strip()
bomb = input().strip()

stack = []

bomb_len = len(bomb)

for s in st:
    stack.append(s)

    if len(stack) >= bomb_len and "".join(stack[-bomb_len:]) == bomb:
        del stack[-bomb_len:]

answer = "".join(stack)
print(answer if answer else "FRULA")
