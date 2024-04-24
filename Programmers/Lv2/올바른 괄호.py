def solution(s):
    bracket = []
    if s[0] == ")":
        return False
    for i in s:
        if i == "(":
            bracket.append(i)
        else:
            if bracket:
                bracket.pop()
            else:
                return False

    if bracket:
        return False
    else:
        return True