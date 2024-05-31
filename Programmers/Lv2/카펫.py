def solution(brown, yellow):
    y_x = 0
    y_y = 0

    for i in range(1, yellow + 1):
        if yellow % i == 0:
            y_x = int(yellow // i)
            y_y = int(yellow // y_x)
            # print(y_x, y_y)
            if (y_x * 2) + (y_y * 2) + 4 == brown:
                # print(y_x, y_y)
                return sorted([y_x + 2, y_y + 2], reverse=True)