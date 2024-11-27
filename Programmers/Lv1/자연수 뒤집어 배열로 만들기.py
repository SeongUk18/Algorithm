def solution(n):
    answer = []
    n = list(reversed(str(n)))
    for i in n:
        answer.append(int(i))

    return answer
