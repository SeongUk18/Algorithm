class AdjacencyMatrix:
    def __init__(self, num_vertices):
        # num_vertices는 그래프의 노드 개수를 의미하며, N x N 행렬을 초기화합니다.
        self.num_vertices = num_vertices
        self.matrix = [
            [0 for _ in range(self.num_vertices)] for _ in range(self.num_vertices)
        ]

    # 간선을 추가하는 함수 (무방향 그래프)
    def add_edge(self, u, v, weight=1):
        # u와 v 노드 간에 weight로 간선을 추가합니다.
        self.matrix[u][v] = weight
        self.matrix[v][u] = weight

    # 간선을 제거하는 함수
    def remove_edge(self, u, v):
        # u와 v 노드 간의 간선을 제거합니다.
        self.matrix[u][v] = 0
        self.matrix[v][u] = 0

    # 특정 노드의 인접 노드 목록을 반환하는 함수
    def get_adjacent_nodes(self, u):
        # u 노드에 연결된 모든 노드들을 반환합니다.
        return [v for v in range(self.num_vertices) if self.matrix[u][v] != 0]

    # 그래프를 출력하는 함수
    def display(self):
        # 현재 인접 행렬을 보기 쉽게 출력합니다.
        for row in self.matrix:
            print(row)


# 그래프 생성 (4개의 노드)
am = AdjacencyMatrix(4)

# 간선 추가
am.add_edge(0, 1)
am.add_edge(0, 2)
am.add_edge(1, 2)
am.add_edge(1, 3)
am.add_edge(2, 3)

# 그래프 출력
am.display()
"""
[0, 1, 1, 0]
[1, 0, 1, 1]
[1, 1, 0, 1]
[0, 1, 1, 0]
"""
# 특정 노드의 인접 노드 출력
print("0번 노드와 인접한 노드들:", am.get_adjacent_nodes(0))
# 0번 노드와 인접한 노드들: [1, 2]
print("1번 노드와 인접한 노드들:", am.get_adjacent_nodes(1))
# 1번 노드와 인접한 노드들: [0, 2, 3]
