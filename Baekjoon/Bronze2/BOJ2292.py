find_num = int(input())


def find(room):
    # number => 최대 갈수 있는 방, dist => 거리
    number = 1
    dist = 1
    while True:
        # 최대 갈수 있는 방보다 작을 때,
        if number >= room:
            return dist
        else:
            # 최대 갈수 있는 방 증가
            number = number + dist * 6
            dist += 1


print(find(find_num))