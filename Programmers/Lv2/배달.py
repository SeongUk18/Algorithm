from collections import defaultdict, deque


def solution(N, road, K):
    answer = 1

    node_dict = defaultdict(list)

    distance = [float('inf') for _ in range(N + 1)]
    distance[1] = 0
    for i, j, dist in road:
        node_dict[i].append((j, dist))
        node_dict[j].append((i, dist))

    q = deque()
    q.append((1, 0))

    while q:
        cur_node, dist = q.popleft()
        for next_node, next_dist in node_dict[cur_node]:
            total_dist = dist + next_dist
            if total_dist <= K and total_dist < distance[next_node]:
                q.append((next_node, total_dist))
                distance[next_node] = total_dist

    # print(distance)
    for i in distance:
        if i <= K and i != 0:
            answer += 1

    return answer
