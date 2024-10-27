from collections import defaultdict, deque


def bfs(start, graph, n):
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[start] = 0
    q = deque([start])

    while q:
        cur_node = q.popleft()
        cur_dist = dist[cur_node]

        for next_node, fare in graph[cur_node]:
            if dist[next_node] > cur_dist + fare:
                dist[next_node] = cur_dist + fare
                q.append(next_node)

    return dist


def solution(n, s, a, b, fares):
    # 그래프 구성
    graph = defaultdict(list)
    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))

    # 1. s(출발지점)에서 각 지점까지의 최단 경로
    dist_from_s = bfs(s, graph, n)

    # 2. a와 b의 최단 경로
    dist_from_a = bfs(a, graph, n)
    dist_from_b = bfs(b, graph, n)

    # 3. 중간 지점 k를 결정하여 최단 비용 계산
    min_cost = float('inf')

    for k in range(1, n + 1):
        # s -> k -> a와 b로 각각 가는 비용 계산
        total_cost = dist_from_s[k] + dist_from_a[k] + dist_from_b[k]
        min_cost = min(min_cost, total_cost)

    return min_cost
