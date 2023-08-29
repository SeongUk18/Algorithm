"""
두 개의 격자 비교하기

n x m 크기의 2차원 격자가 두 개 주어지고, 새로운 2차원 격자를 만들려고 합니다.
주어진 두 격자에서 같은 위치에 존재하는 숫자의 값이 같다면 0, 그렇지 않다면 1을 적어주려 합니다.
새로운 2차원 격자를 만들어 이를 해결하는 프로그램을 작성해보세요.

입력 형식
첫 번째 줄에 격자의 행의 개수 n과, 열의 개수 m이 공백을 두고 주어집니다.
두 번째 줄부터 n개의 줄에 걸쳐 첫 번째 n x m 크기의 격자가 주어집니다.
n + 2 번째 줄부터 n개의 줄에 걸쳐 두 번째 n x m 크기의 격자가 주어집니다.
격자의 정보에 해당하는 각 행에는 m개의 숫자가 공백을 사이에 두고 주어짐을 가정해도 좋습니다.
1 ≤ n, m ≤ 10
1 ≤ 정수 ≤ 10

출력 형식
첫 번째 줄부터 n개의 줄에 걸쳐 새롭게 만든 격자를 출력합니다.

입출력 예제

입력:
4 4
1 4 5 2
3 3 5 2
3 6 2 1
6 2 5 4
3 4 5 2
3 3 2 2
3 6 2 1
6 3 5 4

출력:
1 0 0 0
0 0 1 0
0 0 0 0
0 1 0 0
"""

n, m = map(int, input().split())

first_list = []
second_list = []
final_list = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(n):
    first_list.append(list(map(int, input().split())))
for _ in range(n):
    second_list.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if first_list[i][j] != second_list[i][j]:
            final_list[i][j] = 1

for i in range(n):
    for j in range(m):
        print(final_list[i][j], end=" ")
    print()
