# 시뮬레이션 알고리즘
#### 미완성 ####
n, m = map(int, input().split())

room = []
for _ in range(n):
    room.append(list(map(int, input().split())))


def check_left(room, i, j):
    check = 0
    fill_room = []
    while True:
        if i-1 < 0:
            break
        if room[i-1][j] == 6:
            break
        if room[i-1][j] == 0:
            check += 1
            fill_room.append([i-1, j])
            i -= 1
    return check, fill_room


def check_right(room, i, j):
    check = 0
    fill_room = []
    while True:
        if i+1 >= n:
            break
        if room[i+1][j] == 6:
            break
        if room[i+1][j] == 0:
            check += 1
            fill_room.append([i+1, j])
            i += 1
    return check, fill_room


def check_up(room, i, j):
    check = 0
    fill_room = []
    while True:
        if j-1 < 0:
            break
        if room[i][j-1] == 6:
            break
        if room[i][j-1] == 0:
            check += 1
            fill_room.append([i, j-1])
            j -= 1
    return check, fill_room


def check_down(room, i, j):
    check = 0
    fill_room = []
    while True:
        if j+1 < m:
            break
        if room[i][j+1] == 6:
            break
        if room[i][j+1] == 0:
            check += 1
            fill_room.append([i, j+1])
            j += 1
    return check, fill_room


def fill_room(room, room_list):
    for k in room_list:
        room[k[0]][k[1]] = '#'
    return room


def check_room(room):
    result = 0
    for i in range(n):
        for j in range(m):
            if room[i][j] == 0:
                result += 1
    return result


for i in range(n):
    for j in range(m):
        if room[i][j] == 1:
            left, left_room = check_left(room, i, j)
            right, right_room = check_right(room, i, j)
            up, up_room = check_up(room, i, j)
            down, down_room = check_down(room, i, j)
            wall_number = [left, right, up, down]
            max_wall = max(wall_number)
            fill_place = [left_room, right_room, up_room, down_room]
            fill_room(room, fill_place[wall_number.index(max_wall)])

print(room)

#### 미완성 ####