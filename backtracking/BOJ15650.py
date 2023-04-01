n, m = map(int, input().split())
# 숫자 사용 유무 확인
check_num = [False for _ in range(n+1)]
# 조합 배열
permutation_result = [0 for _ in range(m)]
# 중복 확인 배열
check = []


def permutation(index, p_count, p_length):
    # 중복 체크용 변수
    start = 1
    index_num = 0
    if index == p_length:
        print(*permutation_result)
        return
    for i in range(1, p_count + 1):
        # True면 사용한 숫자
        if check_num[i]:
            continue
        if i in check:
            continue
        # index 칸 채우기
        permutation_result[index] = i
        # 사용했던 숫자 확인해 중복 없앰
        if permutation_result[index_num] == start:
            check.append(start)
            start += 1
        # 사용 체크
        check_num[i] = True
        # 다음 칸 채우기
        permutation(index + 1, p_count, p_length)
        # 사용 해제
        check_num[i] = False
        if p_length == p_count:
            check.append(p_count)


# index == 채울칸
permutation(0, n, m)

