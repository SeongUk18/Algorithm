def solution(n, words):
    answer = []
    word_set = set()
    word_set.add(words[0])
    for i in range(1, len(words)):
        # print(words[i - 1][-1])
        # print(words[i][0])
        if words[i] in word_set or words[i - 1][-1] != words[i][0]:
            answer.append(i % n + 1)
            answer.append(i // n + 1)
            return answer
        else:
            word_set.add(words[i])

    return [0, 0]