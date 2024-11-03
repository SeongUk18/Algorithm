from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0

    bridge = deque([0 for _ in range(bridge_length)])

    truck_weights = deque(truck_weights)
    cur_weight = 0

    while bridge:
        answer += 1
        cur_weight -= bridge.popleft()

        if truck_weights:
            if cur_weight + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge.append(truck)
                cur_weight += truck
            else:
                bridge.append(0)

    return answer
