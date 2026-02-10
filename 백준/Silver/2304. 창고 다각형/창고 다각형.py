n = int(input())

column_list = []

for _ in range(n):
    x ,y = map(int, input().split())

    column_list.append((x, y))

column_list = sorted(column_list, key=lambda x:x[0])

max_height = (0, 0, 0)

for idx, i in enumerate(column_list):
    if i[1] >= max_height[2]:
        max_height = (idx, i[0], i[1])

# print(max_height)

x, y = 0, 0
dist = 0
area = 0

for i in range(max_height[0]):
    if x == 0:
        x = column_list[i][0]
        y = column_list[i][1]

    if y < column_list[i][1]:
        # print(dist, y)
        dist += column_list[i][0] - x
        x = column_list[i][0]
        area += dist * y
        y = column_list[i][1]
        dist = 0        

dist += max_height[1] - x
# print(dist, y)
area += dist * y
# print(area)

x, y = 0, 0
dist = 0

for i in range(n - 1, max_height[0] - 1, -1):
    if x == 0:
        x = column_list[i][0]
        y = column_list[i][1]

    if y < column_list[i][1]:
        dist += x - column_list[i][0]
        area += dist * y
        x = column_list[i][0]
        y = column_list[i][1]
        dist = 0


dist += x - max_height[1]
area += dist * y

print(area + max_height[2])