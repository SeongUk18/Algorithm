import sys
from collections import deque

node_num = int(sys.stdin.readline())

n = int(sys.stdin.readline())

node_list = [[] for _ in range(node_num + 1)]
virus_node = [True] * (node_num + 1)

for _ in range(n):
    i, j = map(int, sys.stdin.readline().split())
    node_list[i].append(j)
    node_list[j].append(i)


def bfs(start):
    q = deque()
    q.append(start)
    virus_node[start] = False
    while q:
        node = q.popleft()
        virus_node[node] = False
        for k in range(len(node_list[node])):
            if virus_node[node_list[node][k]]:
                q.append(node_list[node][k])


bfs(1)

print(virus_node.count(False) - 1) # 1번 빼야해서 -1 진행
