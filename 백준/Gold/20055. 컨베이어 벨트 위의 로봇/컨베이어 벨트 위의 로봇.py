from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

belt = deque(list(map(int, input().split())))

robots = [False] * n
cnt = belt.count(0)
stage = 0

while cnt < k:
    # 회전
    belt.appendleft(belt.pop())
    for i in range(n-1, 0, -1):
        robots[i] = robots[i - 1]
    robots[0] = False
    robots[n - 1] = False  # 내리는 위치에서 즉시 제거

    # 로봇 이동
    for i in range(n - 2, -1, -1):  # n-1은 항상 비어있으므로 n-2부터
        if robots[i] == True and robots[i + 1] == False and belt[i + 1] > 0:
            robots[i + 1] = True
            robots[i] = False
            belt[i + 1] -= 1
            if belt[i + 1] == 0:
                cnt += 1
    robots[n-1] = False  # 이동 후에도 n-1 제거

    # 로봇 위치
    if robots[0] == False and belt[0] > 0:
        belt[0] -= 1
        if belt[0] == 0:
            cnt += 1
        robots[0] = True
    
    # 스테이지 올리기
    stage += 1

print(stage)