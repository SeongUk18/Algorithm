"""
격자에 점 그리기

m개의 점이 주어졌을 때 각각의 점을 n * n 크기의 격자에 번호를 표시하여 출력하는 프로그램을 작성해보세요. 점의 번호는 정보가 따로 주어지진 않고 입력된 순서대로 부여됩니다. 즉 첫 번째로 입력된 점은 1, k번째로 입력된 점은 k입니다.

입력 형식
첫 번째 줄에 격자의 크기를 나타내는 n과 점의 개수를 나타내는 m이 공백을 사이에 두고 주어집니다.
두 번째 줄부터는 m개의 줄에 걸쳐 점의 위치 (r, c)값이 공백을 사이에 두고 주어집니다. (r, c)는 해당 점이 r행 c열에 놓여야 함을 의미합니다. 입력으로 주어지는 모든 점의 위치는 서로 겹치지 않음을 가정해도 좋습니다. (1 ≤ r ≤ n, 1 ≤ c ≤ n)
1 ≤ n ≤ 9
1 ≤ m ≤ n * n

출력 형식
n개의 줄에 걸쳐 각 행에 해당하는 n개의 숫자를 공백을 사이에 두고 출력합니다. 해당 칸에 점이 놓여져 있는 경우라면 점의 번호를 출력하고, 점이 놓여져 있지 않다면 0을 출력합니다.

입출력 예제

입력:
2 3
1 1
1 2
2 2

출력:
1 2
0 3
"""
n, m = map(int, input().split())

answer = [[0 for _ in range(n)]for _ in range(n)]

num = 1
for _ in range(m):
    x, y = map(int, input().split())
    answer[x-1][y-1] = num
    num += 1

for i in range(n):
    for j in range(n):
        print(answer[i][j], end=" ")
    print()