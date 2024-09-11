class AdjacencyList:
    def __init__(self):
        # 그래프를 인접 리스트로 표현하기 위해 딕셔너리를 사용합니다.
        self.list = {}

    # 간선을 추가하는 함수 (무방향 그래프)
    def add_edge(self, u, v):
        # 노드 u에 연결된 리스트에 v를 추가
        if u not in self.list:
            self.list[u] = []
        self.list[u].append(v)

        # 무방향 그래프이므로 노드 v에 u를 추가
        if v not in self.adj_list:
            self.list[v] = []
        self.list[v].append(u)

    # 간선을 제거하는 함수
    def remove_edge(self, u, v):
        # 노드 u에서 v를 제거
        if u in self.list and v in self.list[u]:
            self.list[u].remove(v)

        # 노드 v에서 u를 제거
        if v in self.list and u in self.list[v]:
            self.list[v].remove(u)

    # 특정 노드의 인접 노드 목록을 반환하는 함수
    def get_adjacent_nodes(self, u):
        # 노드 u에 연결된 모든 노드들을 반환
        if u in self.list:
            return self.list[u]
        return []

    # 그래프를 출력하는 함수
    def display(self):
        # 현재 인접 리스트를 보기 쉽게 출력합니다.
        for key in self.list:
            print(f"{key}: {self.list[key]}")


# 그래프 생성
al = AdjacencyList()

# 간선 추가
al.add_edge(0, 1)
al.add_edge(0, 2)
al.add_edge(1, 2)
al.add_edge(1, 3)
al.add_edge(2, 3)

# 그래프 출력
al.display()
"""
0: [1, 2]
1: [0, 2, 3]
2: [0, 1, 3]
3: [1, 2]
"""
# 특정 노드의 인접 노드 출력
print("0번 노드와 인접한 노드들:", al.get_adjacent_nodes(0))
# 0번 노드와 인접한 노드들: [1, 2]
print("1번 노드와 인접한 노드들:", al.get_adjacent_nodes(1))
# 1번 노드와 인접한 노드들: [0, 2, 3]
