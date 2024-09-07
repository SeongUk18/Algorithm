def solution(arr):
    def compress(x, y, size):
        initial_value = arr[x][y]

        # 값 다 같은 지 확인
        for i in range(x, x + size):
            for j in range(y, y + size):
                if arr[i][j] != initial_value:
                    # 다 같지 않으면 4개로 쪼개서 확인
                    half_size = size // 2
                    top_left = compress(x, y, half_size)
                    top_right = compress(x, y + half_size, half_size)
                    bottom_left = compress(x + half_size, y, half_size)
                    bottom_right = compress(x + half_size, y + half_size, half_size)

                    # 4개 섹션 0, 1 수 반환
                    return [top_left[0] + top_right[0] + bottom_left[0] + bottom_right[0],
                            top_left[1] + top_right[1] + bottom_left[1] + bottom_right[1]]

        # 다 같을 때 값 반환
        if initial_value == 0:
            return [1, 0]
        else:
            return [0, 1]

    n = len(arr)
    return compress(0, 0, n)
