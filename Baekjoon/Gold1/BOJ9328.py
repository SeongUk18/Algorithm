from collections import deque


# 들어갈 수 있는 지 확인용 함수
def check(text, i, j):
    global answer

    if text == "*":
        return False

    if text == ".":
        return True

    if text == "$":
        answer += 1
        return True

    if text.islower():  # 열쇠를 찾으면
        keys.add(text)  # 열쇠 추가
        # 열쇠를 얻었으니 지금까지 못 열었던 문들 다시 확인
        temp_last_check = last_check[:]
        for door in temp_last_check:
            if door[0] in keys:
                q.append((door[1], door[2]))
                map_check[door[1]][door[2]] = True
                last_check.remove(door)
        return True

    if text.isupper():  # 문을 만나면
        if text.lower() in keys:  # 열쇠가 있으면 바로 통과
            return True
        else:
            last_check.append((text.lower(), i, j))  # 열쇠가 없으면 나중에 처리
            return False


# 입력 받기
n = int(input())
for k in range(n):
    h, w = map(int, input().split())

    map_list = []

    for _ in range(h):
        map_list.append(list(input()))

    map_check = [[False for _ in range(w)] for _ in range(h)]

    keys_input = input()

    if keys_input == "0":
        keys = set()  # 열쇠가 없는 경우
    else:
        keys = set(list(keys_input))  # 이미 가지고 있는 열쇠 집합

    q = deque()
    answer = 0
    x_list = [0, 0, -1, 1]
    y_list = [-1, 1, 0, 0]

    last_check = []

    # 가장 자리 탐색 (들어갈 수 있는 곳 인지) -> 첫번째 열, 마지막열, 첫번째 행, 마지막 행
    for i in range(w):
        if check(map_list[0][i], 0, i):
            q.append((0, i))
            map_check[0][i] = True

        if check(map_list[h - 1][i], h - 1, i):
            q.append((h - 1, i))
            map_check[h - 1][i] = True

    for i in range(1, h - 1):
        if check(map_list[i][0], i, 0):
            q.append((i, 0))
            map_check[i][0] = True

        if check(map_list[i][w - 1], i, w - 1):
            q.append((i, w - 1))
            map_check[i][w - 1] = True

    # q 꺼내면서 들어가기
    while q:
        x, y = q.popleft()

        for i in range(4):
            cur_x = x + x_list[i]
            cur_y = y + y_list[i]

            if (
                0 <= cur_x < h
                and 0 <= cur_y < w
                and map_check[cur_x][cur_y] == False
                and check(map_list[cur_x][cur_y], cur_x, cur_y)
            ):
                q.append((cur_x, cur_y))
                map_check[cur_x][cur_y] = True

    print(answer)
