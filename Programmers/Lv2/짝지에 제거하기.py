def solution(s):
    stack = []

    for i in s:
        if stack and stack[-1] == i:
            v = stack.pop()
            # print(v)
        else:
            stack.append(i)
    if stack:
        return 0
    else:
        return 1