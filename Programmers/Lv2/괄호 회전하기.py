from collections import deque


def solution(s):
    right = 0
    s = deque(s)
    bracket = []
    if "(" not in s or "{" not in s or "[" not in s:
        return 0
    for i in range(len(s)):
        # print(s)
        if s[0] in "])}":
            word = s.popleft()
            s.append(word)
            check = False
            continue
        for j in s:
            if j == "[":
                bracket.append(j)
            elif j == "{":
                bracket.append(j)
            elif j == "(":
                bracket.append(j)
            elif j == "]":
                if "[" in bracket:
                    bracket.remove("[")
                else:
                    check = False
                    break
            elif j == ")":
                if "(" in bracket:
                    bracket.remove("(")
                else:
                    check = False
                    break
            elif j == "}":
                if "{" in bracket:
                    bracket.remove("{")
                else:
                    check = False
                    break
            if bracket:
                check = False
            else:
                check = True
        if check:
            right += 1
            bracket = []
        else:
            bracket = []
        word = s.popleft()
        s.append(word)

    return right