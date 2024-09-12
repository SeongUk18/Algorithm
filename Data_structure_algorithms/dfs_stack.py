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

    # DFS 스택 기반 구현
    def dfs_iterative(self, start_node):
        visited = set()  # 방문한 노드를 저장하는 집합
        stack = [start_node]  # 스택에 시작 노드를 넣음

        while stack:
            node = stack.pop()  # 스택에서 노드를 꺼냄
            if node not in visited:
                print(node, end=" ")  # 방문한 노드 출력
                visited.add(node)

                # 인접한 노드들을 스택에 추가 (방문하지 않은 노드만)
                for cur_node in self.adj_list[node]:
                    if cur_node not in visited:
                        stack.append(cur_node)


# 그래프 생성
graph = Graph()

# 간선 추가 (무방향 그래프)
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(2, 4)

# DFS 탐색 (스택 기반, 0번 노드에서 시작)
graph.dfs_iterative(0)
# 0 4 2 3 1
