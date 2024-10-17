from collections import deque

# 입력받기
n, m = map(int, input().split())

snake = {}
ladder = {}

# 사다리
for _ in range(n):
    s, e = map(int, input().split())
    ladder[s] = e

# 뱀
for _ in range(m):
    s, e = map(int, input().split())
    snake[s] = e

# 나아가기
map_list = [False for _ in range(101)]

q = deque()

q.append((1, 0))
map_list[1] == True
answer = float("inf")

while q:
    now, dist = q.popleft()

    if now == 100:
        answer = min(answer, dist)
        break

    for i in range(1, 7):
        cur = now + i

        if cur <= 100 and map_list[cur] == False:
            if cur in ladder:
                cur = ladder[cur]

            if cur in snake:
                cur = snake[cur]

            map_list[cur] = True

            q.append((cur, dist + 1))

print(answer)
