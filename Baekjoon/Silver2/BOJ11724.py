import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]  # 입력값 그대로 사용하기 위한 + 1
visited = [False] * (n + 1)

edge_count = 0

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    graph[j].append(i)
    graph[i].append(j)


def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        node = q.popleft()
        for j in graph[node]:
            if not visited[j]:
                visited[j] = True
                q.append(j)


for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
        edge_count += 1


print(edge_count)

