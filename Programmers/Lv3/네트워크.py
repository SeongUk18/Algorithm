def dfs(computers, visited, node):
    visited[node] = True
    for idx, con in enumerate(computers[node]):
        # print(idx, con)
        if con == 1 and not visited[idx]:
            dfs(computers, visited, idx)


def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    for i in range(n):
        # print(computers[i])
        if not visited[i]:
            dfs(computers, visited, i)
            answer += 1

    return answer

# for i, letter in enumerate(['A', 'B', 'C']):
#     print(i, letter)
# 0 A
# 1 B
# 2 C