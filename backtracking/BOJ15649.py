n, m = map(int, input().split())
# 숫자 사용 유무 확인
check_num = [False for _ in range(n+1)]
# 조합 배열
permutation_result = [0 for _ in range(m)]


def permutation(index, p_count, p_length):
    if index == p_length:
        for i in range(p_length):
            # 채워진 칸 출력
            print(permutation_result[i], end=" ")
        print()
        return
    for i in range(1, p_count + 1):
        # True면 사용한 숫자
        if check_num[i]:
            continue
        # index 칸 채우기
        permutation_result[index] = i
        # 사용 체크
        check_num[i] = True
        # 다음 칸 채우기
        permutation(index + 1, p_count, p_length)
        # 사용 해제
        check_num[i] = False


# index == 채울칸
permutation(0, n, m)

