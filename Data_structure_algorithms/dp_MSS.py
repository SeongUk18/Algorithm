def max_subarray_sum(arr):
    # 첫 번째 요소로 초기화
    max_cur = max_global = arr[0]

    # 배열의 두 번째 요소부터 시작해서 순회
    for i in range(1, len(arr)):
        # 현재 요소를 포함한 부분 배열의 최대 합을 계산
        max_cur = max(arr[i], max_cur + arr[i])

        # 전체 최대 합을 업데이트
        if max_cur > max_global:
            max_global = max_cur

    return max_global


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(arr))  # 6
