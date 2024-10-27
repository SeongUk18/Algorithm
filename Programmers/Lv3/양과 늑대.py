from collections import defaultdict
import copy


def solution(info, edges):
    answer = 0

    node_list = defaultdict(list)

    for i, j in edges:
        node_list[i].append(j)

    def dfs(node, sheep, wolf, next_nodes):
        if info[node] == 0:
            sheep += 1
        else:
            wolf += 1

        if sheep <= wolf:
            return 0

        max_sheep = sheep

        for next_node in next_nodes:
            new_nodes = copy.deepcopy(next_nodes)
            new_nodes.remove(next_node)
            new_nodes.extend(node_list[next_node])
            max_sheep = max(max_sheep, dfs(next_node, sheep, wolf, new_nodes))

        return max_sheep

    answer = dfs(0, 0, 0, node_list[0])

    return answer
