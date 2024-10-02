def generate_permutations(nums):
    def backtrack(current_permutation, used):
        # 모든 원소를 사용한 경우, 순열을 저장
        if len(current_permutation) == len(nums):
            result.append(list(current_permutation))
            return

        # 가능한 모든 원소를 탐색
        for i in range(len(nums)):
            if used[i]:  # 이미 사용한 원소는 패스
                continue

            # 현재 원소를 순열에 추가
            current_permutation.append(nums[i])
            used[i] = True  # 현재 원소를 사용했음을 표시

            # 재귀적으로 나머지 원소들에 대해 순열 생성
            backtrack(current_permutation, used)

            # 백트래킹: 원래 상태로 되돌리기
            current_permutation.pop()
            used[i] = False

    result = []
    used = [False] * len(nums)  # 원소 사용 여부를 기록
    backtrack([], used)  # 빈 순열로 시작
    return result


# 테스트
nums = [1, 2, 3]
print(generate_permutations(nums))
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
