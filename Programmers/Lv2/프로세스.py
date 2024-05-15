from collections import deque


def solution(priorities, location):
    answer = 0
    q = deque((i, j) for i, j in enumerate(priorities))
    # print(q)
    while q:
        cur = q.popleft()
        if any(cur[1] < que[1] for que in q):
            q.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

# any() : 하나라도 True인게 있으면 True
# all() : 모두 True여야 True 반환
