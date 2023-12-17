import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

map_list = []
dx = (1, -1, 0, 0)
dy = (0, 0, -1, 1)
dist = 0
visited = [[False for _ in range(m)] for _ in range(n)]

for _ in range(n):
    map_list.append(list(sys.stdin.readline()))


def bfs(start_y, start_x):
    q = deque()
    q.append((start_y, start_x, 1)) # 거리를 계산 하기 위한 Q에 3번째 인자
    while q:
        y, x, dist = q.popleft()
        if visited[y][x]:
            continue
        visited[y][x] = True
        map_list[y][x] = dist
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[ny][nx] and map_list[ny][nx] != "0":
                    q.append((ny, nx, dist + 1))
            else:
                continue


for i in range(n):
    for j in range(m):
        if map_list[i][j] == "0" and not visited[i][j]:
            continue
        else:
            bfs(i, j)


print(map_list[n-1][m-1])