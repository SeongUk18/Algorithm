def solution(s):
    # {,} 제거
    s = s.lstrip('{').rstrip('}').split('},{')
    # , 제거 및 값 내부 셋 추출
    s_set = [set(map(int, x.split(','))) for x in s]
    s_set.sort(key=len)

    answer = []
    # print(s_set)
    # 집합 원소 확인
    for num in s_set:
        answer.extend(list(num - set(answer)))

    return answer
