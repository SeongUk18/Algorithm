from collections import deque, defaultdict


def bfs(graph, start, n):
    visited = [False for _ in range(n + 1)]
    q = deque([start])
    visited[start] = True
    count = 1

    while q:
        node = q.popleft()
        for cur in graph[node]:
            if not visited[cur]:
                visited[cur] = True
                q.append(cur)
                count += 1

    return count


def solution(n, wires):
    # 그래프 인접 리스트로 변환
    graph = defaultdict(list)
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    answer = float('inf')

    # 선 끊기
    for v1, v2 in wires:
        graph[v1].remove(v2)
        graph[v2].remove(v1)

        # 트리 길이 탐색
        tree_size = bfs(graph, v1, n)
        diff = abs(tree_size - (n - tree_size))

        # 차이 계산
        answer = min(diff, answer)

        # 다시 이어놓기
        graph[v1].append(v2)
        graph[v2].append(v1)

    return answer
