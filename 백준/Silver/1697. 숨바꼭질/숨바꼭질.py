from collections import deque

n, k = map(int, input().split())

answer = 0
q = deque()
visited = [False] * 100001

q.append((n, 0))
visited[n] = True

while q:
    now, dist = q.popleft()

    if now == k:
        answer = dist
        break

    if 0 < now and visited[now - 1] == False:
        visited[now - 1] = True
        q.append((now - 1, dist + 1))

    if now < 100000 and visited[now + 1] == False:
        visited[now + 1] = True
        q.append((now + 1, dist + 1))

    if 2 * now <= 100000 and visited[now * 2] == False:
        visited[now * 2] = True
        q.append((now * 2, dist + 1))

print(answer)