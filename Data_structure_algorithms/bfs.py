from collections import deque


class Graph:
    def __init__(self):
        self.adj_list = {}  # 인접 리스트로 그래프 표현

    # 간선 추가 함수
    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)  # 무방향 그래프일 경우

    # BFS 구현
    def bfs(self, start_node):
        visited = set()  # 방문한 노드를 저장하는 집합
        queue = deque()
        queue.append(start_node)  # 큐에 시작 노드를 추가
        visited.add(start_node)  # 시작 노드를 방문 처리

        while queue:
            node = queue.popleft()  # 큐에서 노드를 꺼냄
            print(node, end=" ")

            # 인접한 노드들을 큐에 추가 (방문하지 않은 노드만)
            for cur_node in self.adj_list[node]:
                if cur_node not in visited:
                    queue.append(cur_node)  # 큐에 추가
                    visited.add(cur_node)  # 방문 처리


# 그래프 생성
graph = Graph()

# 간선 추가 (무방향 그래프)
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(2, 4)

# BFS 탐색 (0번 노드에서 시작)
graph.bfs(0)
# 0 1 4 2 3
