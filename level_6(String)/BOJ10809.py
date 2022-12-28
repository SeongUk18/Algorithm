def checking(word):
    # a~z 까지 문자열 생성
    a_to_z = "abcdefghijklmnopqrstuvwxyz"
    result = []
    # 문자열 하나씩 비교
    for i in a_to_z:
        # 없으면 -1 삽입
        if i not in word:
            result.append("-1")
            continue
        else:  # 있으면 해당 인덱스 삽입
            result.append(str(word.index(i)))
    return result


result = checking(input())
print(" ".join(result))