from collections import deque


def solution(maps):
    answer = 0
    map_check = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    x_list = [0, 0, -1, 1]
    y_list = [-1, 1, 0, 0]
    q = deque()
    q.append((0, 0, 1))

    while q:
        x, y, dist = q.popleft()
        for i in range(len(x_list)):
            cur_x = x + x_list[i]
            cur_y = y + y_list[i]

            if 0 <= cur_x < len(maps[0]) and 0 <= cur_y < len(maps) and not map_check[cur_y][cur_x] and maps[cur_y][
                cur_x] != 0:
                q.append((cur_x, cur_y, dist + 1))
                map_check[cur_y][cur_x] = True
                maps[cur_y][cur_x] = dist
                if cur_x == len(maps[0]) - 1 and cur_y == len(maps) - 1:
                    return dist + 1
    return -1