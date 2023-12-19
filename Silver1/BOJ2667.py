import sys
from collections import deque

n = int(sys.stdin.readline())

map_list = []
visited = [[True for _ in range(n)] for _ in range(n)]
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)
number = 1

for _ in range(n):
    map_list.append(list(sys.stdin.readline().strip()))


def bfs(start_y, start_x, number):  # 단지 번호를 위한 3번째 인자
    q = deque()
    q.append((start_y, start_x))

    while q:
        y, x = q.popleft()
        if not visited[y][x]:
            continue
        map_list[y][x] = number
        visited[y][x] = False
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] and map_list[ny][nx] == "1":
                q.append((ny, nx))


for i in range(n):
    for j in range(n):
        if map_list[i][j] == "1" and visited[i][j]:
            bfs(i, j, number)
            number += 1

# print(map_list)
print(number - 1)  # 단지 번호가 마지막에 1 증가 되어 1 빼줌
count = {home: 0 for home in range(1, number)}  # 단지 갯수 확인을 위한 dic
for m_list in map_list:  # 단지 갯수 확인
    for check in m_list:
        if check in count:
            count[check] += 1
count_val = list(count.values())  # 단지 수가 적은 순으로 정렬
count_val.sort()
for i in count_val:  # 결과 출력용
    print(i)
