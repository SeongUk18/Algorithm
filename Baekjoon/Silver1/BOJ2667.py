from collections import deque

n = int(input())

map_list = []

for _ in range(n):
    map_list.append(list(map(int, input().strip())))

visited = [[False for _ in range(n)] for _ in range(n)]

x_list = [0, 0, -1, 1]
y_list = [-1, 1, 0, 0]


def bfs(nx, ny, n):
    q = deque()
    q.append((nx, ny))
    visited[nx][ny] = True
    area = 1

    while q:
        x, y = q.popleft()

        for k in range(4):
            cur_x = x + x_list[k]
            cur_y = y + y_list[k]

            if (
                0 <= cur_x < n
                and 0 <= cur_y < n
                and visited[cur_x][cur_y] == False
                and map_list[cur_x][cur_y] == 1
            ):
                area += 1
                q.append((cur_x, cur_y))
                visited[cur_x][cur_y] = True

    return area


count = 0
answer = []

for i in range(n):
    for j in range(n):
        if map_list[i][j] == 1 and visited[i][j] == False:
            count += 1
            answer.append(bfs(i, j, n))

answer.sort()
print(count)
for i in answer:
    print(i)
