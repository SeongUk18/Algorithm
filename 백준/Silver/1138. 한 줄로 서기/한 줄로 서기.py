n = int(input())

line = list(map(int, input().split()))

answer = []

for i in range(n - 1, -1, -1):
    big = 0

    if line[i] == 0:
        answer = [i + 1] + answer
    else:
        for k in range(len(answer)):
            if answer[k] >= i + 1:
                big += 1
            if big == line[i]:
                answer.insert(k + 1, i + 1)
        # print(big, answer)
# print(answer)

for i in answer:
    print(i, end=" ")