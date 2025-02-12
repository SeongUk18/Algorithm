from collections import deque


def solution(skill, skill_trees):
    answer = 0

    def check(able, s):
        for i in range(len(skill)):
            if able[i] == False:
                if skill[i] == s:
                    able[i] = True
                    return True
                else:
                    return False

    for tech in skill_trees:
        able = [False for _ in range(len(skill))]
        for s in tech:
            if s in skill:
                # print(able, s)
                if check(able, s) == False:
                    break
            if tech[-1] == s:
                answer += 1

    return answer