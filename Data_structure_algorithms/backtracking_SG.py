def generate_subsets(nums):
    def backtrack(start, current_subset):
        # 현재까지 만든 부분 집합을 결과에 추가
        result.append(list(current_subset))

        # start부터 끝까지 모든 요소를 확인
        for i in range(start, len(nums)):
            # 현재 요소를 부분 집합에 추가
            current_subset.append(nums[i])
            # 재귀적으로 다음 원소에 대해 백트래킹
            backtrack(i + 1, current_subset)
            # 백트래킹: 원래 상태로 되돌리기 위해 마지막 요소 제거
            current_subset.pop()

    result = []
    backtrack(0, [])  # 0번째 원소부터 탐색 시작, 빈 부분 집합에서 시작
    return result


# 테스트
nums = [1, 2, 3]
print(generate_subsets(nums))
# [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
