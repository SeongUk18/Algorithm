from collections import deque

n, w, l = map(int, input().split())

truck_weights = list(map(int, input().split()))

bridge = deque([0 for _ in range(w)])
truck_weights = deque(truck_weights)
cur_weight = 0
answer = 0

while bridge:
    cur_weight -= bridge.popleft()
    answer += 1

    if truck_weights:
        if cur_weight + truck_weights[0] <= l:
            truck = truck_weights.popleft()
            cur_weight += truck
            bridge.append(truck)
        else:
            bridge.append(0)

print(answer)
