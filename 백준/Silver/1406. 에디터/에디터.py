from collections import deque
import sys

input = sys.stdin.readline

right = deque()
left = deque(list(input().strip()))

n = int(input())

def move_left():
    if left:
        s = left.pop()
        right.appendleft(s)

def move_right():
    if right:
        s = right.popleft()
        left.append(s)

def delete():
    if left:
        left.pop()

def post(x):
    left.append(x)


for _ in range(n):
    command = input()

    if command[0] == "P":
        post(command[2])
    if command[0] == "L":
        move_left()
    if command[0] == "D":
        move_right()
    if command[0] == "B":
        delete()

# print(left + right)
answer = left + right
for i in answer:
    print(i, end="")