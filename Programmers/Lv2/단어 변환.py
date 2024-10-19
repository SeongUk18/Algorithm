from collections import deque


# 단어 다른 갯수 확인 (변환 가능한지 확인)
def check(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1

    return count == 1


def solution(begin, target, words):
    answer = 0
    visited = [False] * len(words)
    if target not in words:
        return 0

    q = deque([(begin, 0)])  # 시작 단어, 바뀌는 횟수

    while q:
        cur_word, step = q.popleft()

        if cur_word == target:
            return step

        for i in range(len(words)):
            # 단어 확인
            if check(cur_word, words[i]) and not visited[i]:
                visited[i] = True
                q.append((words[i], step + 1))

    return 0
