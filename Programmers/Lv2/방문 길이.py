def solution(dirs):
    answer = 0
    start_x = 5
    start_y = 5
    path = set()
    for i in dirs:
        if i == "U":
            if start_y == 0:
                continue
            else:
                path.add((start_x, start_y, start_x, start_y - 1))
                path.add((start_x, start_y - 1, start_x, start_y))
                start_y -= 1
        elif i == "D":
            if start_y == 10:
                continue
            else:
                path.add((start_x, start_y, start_x, start_y + 1))
                path.add((start_x, start_y + 1, start_x, start_y))
                start_y += 1
        elif i == "R":
            if start_x == 10:
                continue
            else:
                path.add((start_x + 1, start_y, start_x, start_y))
                path.add((start_x, start_y, start_x + 1, start_y))
                start_x += 1
        elif i == "L":
            if start_x == 0:
                continue
            else:
                path.add((start_x - 1, start_y, start_x, start_y))
                path.add((start_x, start_y, start_x - 1, start_y))
                start_x -= 1
    print(path)
    answer = len(path) / 2
    return answer