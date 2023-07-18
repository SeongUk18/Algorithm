def solve(a: int, b: int):
    result = int(b * 100 // a)
    if result >= 99:
        return -1
    # 이진 탐색용 코드
    left, right, now = 1, a, a
    while right >= left:
        mid = (right + left) // 2
        if int((b + mid) * 100 // (a + mid)) > result:
            now = mid
            right = mid - 1
        else:
            left = mid + 1
    return now


a, b = map(int, input().split())
print(solve(a, b))
