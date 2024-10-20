from collections import deque


def bfs(i, j, board, map_check):
    q = deque()
    q.append((i, j, 0))
    map_check[i][j] = True

    while q:
        x, y, dist = q.popleft()

        if board[x][y] == "G":
            return dist

        # 위쪽으로 미끄러짐
        cur_x = x
        while cur_x > 0 and board[cur_x - 1][y] != "D":
            cur_x -= 1
        if map_check[cur_x][y] == False:
            q.append((cur_x, y, dist + 1))
            map_check[cur_x][y] = True

        # 아래쪽으로 미끄러짐
        cur_x = x
        while cur_x < len(board) - 1 and board[cur_x + 1][y] != "D":
            cur_x += 1
        if map_check[cur_x][y] == False:
            q.append((cur_x, y, dist + 1))
            map_check[cur_x][y] = True

        # 왼쪽으로 미끄러짐
        cur_y = y
        while cur_y > 0 and board[x][cur_y - 1] != "D":
            cur_y -= 1
        if map_check[x][cur_y] == False:
            q.append((x, cur_y, dist + 1))
            map_check[x][cur_y] = True

        # 오른쪽으로 미끄러짐
        cur_y = y
        while cur_y < len(board[0]) - 1 and board[x][cur_y + 1] != "D":
            cur_y += 1
        if map_check[x][cur_y] == False:
            q.append((x, cur_y, dist + 1))
            map_check[x][cur_y] = True

    return -1


def solution(board):
    answer = 0
    map_check = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "R":
                answer = bfs(i, j, board, map_check)
                break

    return answer
