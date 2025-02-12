def solution(n, build_frame):
    answer = []

    def check(answer):
        for x, y, a in answer:
            if a == 0:
                if y == 0 or (x - 1, y, 1) in answer or (x, y, 1) in answer or (x, y - 1, 0) in answer:
                    continue
                else:
                    return False

            elif a == 1:
                if (x, y - 1, 0) in answer or (x + 1, y - 1, 0) in answer or (
                        (x - 1, y, 1) in answer and (x + 1, y, 1) in answer):
                    continue
                else:
                    return False
        return True

    for build in build_frame:
        x, y, a, b = build
        if b == 1:
            answer.append((x, y, a))
            if check(answer) == False:
                answer.remove((x, y, a))


        elif b == 0:
            answer.remove((x, y, a))
            if check(answer) == False:
                answer.append((x, y, a))
    answer.sort()
    print(answer)

    return answer
