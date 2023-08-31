"""
파스칼의 삼각형

행의 크기가 정수 n으로 주어집니다. 행의 크기가 n인 파스칼 삼각형을 출력하는 프로그램을 작성해보세요. 파스칼 삼각형이란 다음과 같은 형태로 나타나며, (i, j)에 적힌 숫자가 (i - 1, j - 1)에 적힌 숫자와 (i - 1, j)에 적힌 숫자의 합으로 나타납니다.
n = 5일때의 예
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1

입력 형식
첫 번째 줄에 n이 주어집니다.
1 ≤ n ≤ 15

출력 형식
행의 크기가 n인 파스칼의 삼각형을 입출력 예제와 같이 출력합니다.

입출력 예제

입력:
6
출력:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
"""
n = int(input())

answer =[[0 for _ in range(n)]for _ in range(n)]

for i in range(n):
    answer[i][0] = 1

for i in range(1, n):
    for j in range(1, n):
        answer[i][j] = answer[i-1][j] + answer[i-1][j-1]

for i in range(n):
    for j in range(n):
        if answer[i][j] == 0:
            continue
        else:
            print(answer[i][j], end=" ")
    print()

