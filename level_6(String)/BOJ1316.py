num = int(input())


# 그룹 문자 확인용 함수
def group_words(words):
    for i in range(len(words)):
        # out of range 방지용
        if i < len(words)-2:
            #다음 문자와 같은지 확인
            if words[i] == words[i+1]:
                #같다면 제거
                words.pop(i)
                continue
            #다음 문자와 다른데 문자가 2개이상 있으면 그룹문자가 아님
            elif words.count(words[i]) > 1:
                return 0
    return 1


answer = 0
for _ in range(num):
    # 함수에 넣을 시 리스트 형태로 저장
    answer += group_words(list(input()))
print(answer)