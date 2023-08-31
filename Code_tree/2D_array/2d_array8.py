"""
격자로 사각형 만들기

아래 조건을 만족하도록 격자를 만들어 출력하는 프로그램을 작성해보세요.
첫 번째 행과 첫 번째 열에는 모두 1이 들어갑니다.
나머지 칸들은 바로 위의 값과 바로 왼쪽 값, 그리고 왼쪽 위의 값의 합이 되어야 합니다.
크기는 n x n 입니다.

입력 형식
첫 번째 줄에 정수 n이 주어집니다.
2 ≤ n ≤ 10

출력 형식
첫 번째 줄부터 n개의 줄에 걸쳐, 각 행에 해당하는 n개의 수를 공백을 사이에 두고 출력합니다.

입출력 예제
입력:
5

출력:
1 1 1 1 1
1 3 5 7 9
1 5 13 25 41
1 7 25 63 129
1 9 41 129 321
"""
n = int(input())

answer = [[0 for _ in range(n)]for _ in range(n)]

for i in range(n):
    answer[i][0] = 1
    answer[0][i] = 1

for i in range(1, n):
    for j in range(1, n):
        answer[i][j] = answer[i-1][j] + answer[i-1][j-1] + answer[i][j-1]

for i in range(n):
    for j in range(n):
        print(answer[i][j], end=" ")
    print()