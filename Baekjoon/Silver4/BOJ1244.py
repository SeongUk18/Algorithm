N = int(input())

sensor_list = list(map(int, input().split()))
people_n = int(input())
sensor_list = [0] + sensor_list
people = []

for _ in range(people_n):
    people.append(list(map(int, input().split())))


def switch(i):
    if sensor_list[i] == 1:
        sensor_list[i] = 0
    else:
        sensor_list[i] = 1


def man(num):
    i = num
    while i <= N:
        switch(i)
        i += num


def woman(num):
    left = right = num  # 중심 위치 설정

    while True:
        # 1. 왼쪽으로 한 칸 이동 가능한지 확인
        if left - 1 < 1:
            break  # 왼쪽 범위 벗어나면 종료

        # 2. 오른쪽으로 한 칸 이동 가능한지 확인
        if right + 1 > N:
            break  # 오른쪽 범위 벗어나면 종료

        # 3. 좌우 값이 같은지 확인
        if sensor_list[left - 1] != sensor_list[right + 1]:
            break  # 좌우 대칭 아니면 종료

        # 4. 위 조건 다 만족하면 좌우 한 칸씩 확장
        left -= 1
        right += 1

    # 5. 최종 확정된 범위 [left ~ right] 토글
    for i in range(left, right + 1):
        switch(i)


for order in people:
    p, num = order
    if p == 1:
        man(num)
    else:
        woman(num)


for i in range(1, N + 1):
    print(sensor_list[i], end=' ')
    if i % 20 == 0:
        print()
