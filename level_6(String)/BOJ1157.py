S = input()


def find(word):
    # 대문자로 변경
    word = word.upper()
    # 딕셔너리 활용
    st = {}
    for i in word:
        if i not in st:
            #딕셔너리 이용하여 key : 문자 value : 갯수 설정
            st[i] = word.count(i)
    # 최대 갯수, 최대 갯수 반복 수, 최대 갯수 문자 변수 생성
    max_w = max(st.values())
    max_n = 0
    result = ""
    for i in st:
        # 최대 갯수 문자면 반복 수 증가, 갯수 문자 변경
        if st[i] == max_w:
            max_n += 1
            result = i
    # 최대 갯수 반복 수가 1 초과면 -> 여러개
    if max_n > 1:
        return "?"
    else:
        return result


print(find(S))