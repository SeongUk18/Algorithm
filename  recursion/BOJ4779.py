import sys
sys.setrecursionlimit(10 ** 6)


# 재귀 부분
def cantorian_set(line):
    # 1이면 - 츨력 0이면 공백 출력
    if line == "1":
        return "-"
    elif line == "0":
        return " "
    else:
        line1 = line[0:len(line)//3]
        line2 = line[len(line)//3:len(line)*2//3]
        line2 = erase(line2)
        line3 = line[len(line)*2//3:]
        return cantorian_set(line1) + cantorian_set(line2) + cantorian_set(line3)


# 문자 지우기
def erase(lines):
    return "0"*len(lines)


while True:
    try:
        N = int(input())
        # 입력 없을 때,
        if N == '':
            break
        result = cantorian_set(pow(3, N)*"1")
        print(result)
    except EOFError:
        break
