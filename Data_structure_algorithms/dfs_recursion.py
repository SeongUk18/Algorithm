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

    # DFS 재귀 구현
    def dfs(self, node, visited):
        # 현재 노드를 방문 처리
        visited.add(node)
        print(node, end=" ")  # 방문한 노드 출력

        # 인접 노드들 중 방문하지 않은 노드들을 재귀적으로 탐색
        for cur_node in self.adj_list[node]:
            if cur_node not in visited:
                self.dfs(cur_node, visited)

    # 그래프 탐색을 시작하는 함수
    def dfs_start(self, start_node):
        visited = set()  # 방문한 노드를 저장하는 집합
        self.dfs(start_node, visited)


# 그래프 생성
graph = Graph()

# 간선 추가 (무방향 그래프)
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(2, 4)

# DFS 탐색 (0번 노드에서 시작)
graph.dfs_start(0)
# 0 1 2 3 4
