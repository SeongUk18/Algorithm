def solution(absolutes, signs):
    answer = 0

    for num, sigh in zip(absolutes, signs):
        if sigh:
            answer += num
        else:
            answer -= num
    return answer
