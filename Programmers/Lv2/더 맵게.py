import heapq as hq


def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)

    while len(scoville) > 1:
        cur = hq.heappop(scoville)
        pre_s = hq.heappop(scoville)
        # print(cur, pre_s)
        if pre_s >= K and cur >= K:
            return answer

        if cur > pre_s:
            last = cur
            new = pre_s + cur * 2
            answer += 1
            if len(scoville) == 0 and new >= K:
                return answer
            hq.heappush(scoville, new)
        else:
            last = pre_s
            new = cur + pre_s * 2
            answer += 1
            if len(scoville) == 0 and new >= K:
                return answer
            hq.heappush(scoville, new)

        if new >= K and last >= K:
            return answer

    cur = hq.heappop(scoville)
    # print("-------------------")
    # print(last, cur)

    if cur > pre_s:
        pre_s = pre_s + cur * 2
        answer += 1
    else:
        cur = cur + pre_s * 2
        answer += 1

    if pre_s >= K and cur >= K:
        return answer
    else:
        return -1


