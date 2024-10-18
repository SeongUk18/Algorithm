import heapq  # 우선순위 큐를 위한 heapq 모듈 사용


def dijkstra(graph, start):
    # 각 노드까지의 최단 거리를 저장하는 딕셔너리 (초기값: 무한대)
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    # 우선순위 큐를 사용해 최단 경로를 가진 노드를 선택
    pq = [(0, start)]

    while pq:
        cur_dist, cur_node = heapq.heappop(pq)

        # 현재 노드까지의 거리가 기존 거리보다 크면 무시
        if cur_dist > dist[cur_node]:
            continue

        # 현재 노드와 연결된 다른 노드들에 대해 거리를 계산
        for neighbor, weight in graph[cur_node].items():
            distance = cur_dist + weight

            # 새로운 경로가 더 짧으면 최단 거리 갱신
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return dist


# 테스트를 위한 그래프
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2},
    'C': {'A': 4, 'E': 1},
    'D': {'B': 2, 'E': 5},
    'E': {'C': 1, 'D': 5}
}

# A 노드에서 시작하여 다른 노드들까지의 최단 거리 계산
print(dijkstra(graph, 'A'))