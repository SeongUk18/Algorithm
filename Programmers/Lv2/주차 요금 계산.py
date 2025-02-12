import math
from collections import defaultdict


def time_to_min(time):
    hour = time[:2]
    mini = time[3:]
    # print(hour, mini)

    return int(hour) * 60 + int(mini)


def solution(fees, records):
    answer = []

    normal_time, normal_cost, d_time, d_cost = fees
    # print(normal_time, normal_cost, d_time, d_cost)

    car_dict = {}
    car_time = defaultdict(int)
    for r in records:
        time, number, command = r.split()
        if command == "IN":
            car_dict[number] = time_to_min(time)

        elif command == "OUT":
            end_time = time_to_min(time)
            start_time = car_dict[number]
            time = end_time - start_time
            car_time[number] += time
            del car_dict[number]

    if car_dict:
        for number, time in car_dict.items():
            end_time = 23 * 60 + 59
            start_time = time
            time = end_time - start_time
            car_time[number] += time
    # print(car_time)
    car_cost = {}

    for number, time in car_time.items():
        if time <= normal_time:
            car_cost[int(number)] = normal_cost
        else:
            cost = normal_cost + math.ceil((time - normal_time) / d_time) * d_cost
            car_cost[int(number)] = cost
    car_cost = sorted(car_cost.items())
    # print(car_cost)
    return [a[1] for a in car_cost]