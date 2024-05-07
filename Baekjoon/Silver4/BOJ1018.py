n, m = map(int, input().split())

map_list = []
# 최대값으로 초기화
answer = 64
for _ in range(n):
    map_list.append(list(input()))


def search(y, x):
    wrong1 = 0
    wrong2 = 0
    for i in range(y, y + 8):
        for j in range(x, x + 8):
            if (i + j) % 2 == 0:
                if map_list[i][j] != 'B':
                    wrong1 += 1
                if map_list[i][j] != 'W':
                    wrong2 += 1
            else:
                if map_list[i][j] != 'B':
                    wrong2 += 1
                if map_list[i][j] != 'W':
                    wrong1 += 1
    # 맞거나 잘못된 타일 수 세기
    return min(wrong1, wrong2)


for y in range(n - 7):
    for x in range(m - 7):
        answer = min(answer, search(y, x))

print(answer)


