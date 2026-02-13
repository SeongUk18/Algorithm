from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = []
start = None

for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)
    for j in range(m):
        if row[j] == 2:
            start = (i, j)

dist = [[-1] * m for _ in range(n)]

# 갈 수 없는 땅(0)은 0으로 출력
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            dist[i][j] = 0

# BFS
q = deque()
q.append(start)
dist[start[0]][start[1]] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    x, y = q.popleft()
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1 and grid[nx][ny] != 0:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

for i in range(n):
    for j in range(m):
        print(dist[i][j], end=" ")
    print()