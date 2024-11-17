def solution(diffs, times, limit):
    def can_complete(level):
        # 숙련도 level로 제한 시간 내에 퍼즐을 해결할 수 있는지 확인
        total_time = 0
        time_prev = 0

        for diff, time_cur in zip(diffs, times):
            if level >= diff:
                # 틀리지 않고 해결
                total_time += time_cur
            else:
                # (diff - level)번 틀림
                mistakes = diff - level
                total_time += mistakes * (time_cur + time_prev) + time_cur

            # 현재 퍼즐의 소요 시간을 이전 퍼즐 시간으로 업데이트
            time_prev = time_cur

            if total_time > limit:
                return False

        return total_time <= limit

    # 이분 탐색으로 최소 숙련도 찾기
    left, right = 1, max(diffs)
    answer = right

    while left <= right:
        mid = (left + right) // 2
        if can_complete(mid):
            answer = mid
            right = mid - 1  # 더 낮은 숙련도를 찾는다
        else:
            left = mid + 1  # 더 높은 숙련도를 찾는다

    return answer
