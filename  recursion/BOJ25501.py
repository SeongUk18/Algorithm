# palindrome 인지 확인
def is_palindrome(string_name):
    # 재귀 횟수 확인용
    count = 1
    return recursion(string_name, 0, len(string_name)-1, count)


# 재귀 부분
def recursion(string_name, start, end, count):
    if start >= end:
        return 1, count
    elif string_name[start] != string_name[end]:
        return 0, count
    else:
        return recursion(string_name, start+1, end-1, count+1)


N = int(input())
for _ in range(N):
    pali, recount = is_palindrome(input())
    print(pali, recount)