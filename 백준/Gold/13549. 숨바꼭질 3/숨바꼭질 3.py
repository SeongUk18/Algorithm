from collections import deque

n, k = map(int, input().split())

q = deque()
visited = [float('inf')] * 100001

q.append((n, 0))
visited[n] = 0

while q:
    now, dist = q.popleft()

    if 0 < now and visited[now - 1] > dist + 1:
        visited[now - 1] = dist + 1
        q.append((now - 1, dist + 1))

    if now < 100000 and visited[now + 1] > dist + 1:
        visited[now + 1] = dist + 1
        q.append((now + 1, dist + 1))

    if 2 * now <= 100000 and visited[now * 2] > dist:
        visited[now * 2] = dist
        q.appendleft((now * 2, dist))

print(visited[k])