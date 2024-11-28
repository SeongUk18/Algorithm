def solution(x):
    n = sum([int(i) for i in str(x)])

    if x % n == 0:
        return True
    else:
        return False
