def solution(n):
    answer = []
    direction = [(1, 0), (0, 1), (-1, -1)]
    total = 0
    for i in range(1, n + 1):
        total += i
    # print(total)
    start_direction = 0

    tower = [[0] * i for i in range(1, n + 1)]
    # print(tower)
    start_x = 0
    start_y = 0
    for i in range(1, total + 1):
        tower[start_x][start_y] = i

        # 다음 위치 계산
        next_x = start_x + direction[start_direction][0]
        next_y = start_y + direction[start_direction][1]

        # 다음 위치가 벗어낫거나 이미 채워져 있으면 방향 변경
        if not (0 <= next_x < len(tower) and 0 <= next_y < len(tower[next_x])) or tower[next_x][next_y] != 0:
            start_direction = (start_direction + 1) % 3

            next_x = start_x + direction[start_direction][0]
            next_y = start_y + direction[start_direction][1]

        start_x, start_y = next_x, next_y

    # print(tower)

    # 일차원으로 변경
    for i in tower:
        answer += i

    return answer
