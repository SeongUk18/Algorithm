from collections import deque, defaultdict


def solution(n, path, order):
    path_dict = defaultdict(list)
    order_first = defaultdict(int)
    order_last = defaultdict(int)

    visited = [False] * n
    for v1, v2 in path:
        path_dict[v1].append(v2)
        path_dict[v2].append(v1)

    for v1, v2 in order:
        order_first[v1] = v2
        order_last[v2] = v1

    # print(path_dict)
    # print(order_first)
    # print(order_last)

    if 0 in order_last:
        return False

    q = deque()
    q.append(0)
    visited[0] = True
    wait = {}

    while q:
        room = q.popleft()

        if room in order_first:
            last = order_first[room]
            if last in wait:
                q.append(last)
                visited[last] = True
                del wait[last]

        for cur in path_dict[room]:
            if not visited[cur]:
                if cur in order_last and not visited[order_last[cur]]:
                    wait[cur] = True
                else:
                    q.append(cur)
                    visited[cur] = True

        # print(q)

    return all(visited)
