def solution(n):
    n = int("".join(sorted(list(str(n)), reverse = True)))
    return n
