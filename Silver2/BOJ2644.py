import sys
from collections import deque

n = int(sys.stdin.readline())

target_x, target_y = map(int, sys.stdin.readline().split())

m = int(sys.stdin.readline())

family = [[] for _ in range(n + 1)]
family_chk = [0 for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    family[x].append(y)
    family[y].append(x)


def bfs(start, dist):
    q = deque()
    q.append([start, dist])
    while q:
        member, number = q.popleft()
        family_chk[member] = number
        if family[member]:
            for k in family[member]:
                if family_chk[k] == 0:
                    q.append([k, number + 1])


# for i in range(1, m + 1):
#     if family_chk[i] == 0:
#         bfs(i, 1)

bfs(target_x, 0)

if family_chk[target_y] == 0:
    print(-1)
else:
    print(family_chk[target_y])