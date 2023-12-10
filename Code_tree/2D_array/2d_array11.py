"""
격자 모양 출력하기

n x n 크기의 격자의 칸 위에 m 개의 점이 놓여져 있습니다.
각 점의 크기는 해당 칸의 행 번호와 열 번호의 곱이 됩니다.
각 점의 위치에 해당하는 정보가 주어질 때, 격자의 모양을 출력하는 프로그램을 작성해보세요.
단, 행과 열의 번호는 1부터 시작됩니다.

입력 형식
첫 번째 줄에 격자의 크기 n과 점의 개수 m이 공백을 두고 주어집니다.
두 번째 줄부터 m개의 줄에 걸쳐 각 점의 행 번호와 열 번호가 공백을 사이에 두고 주어집니다.
주어진 m개의 점의 위치는 모두 다름을 가정해도 좋습니다.
1 ≤ n ≤ 10
1 ≤ m ≤ n * n

출력 형식
첫 번째 줄부터 n개의 줄에 걸쳐, 각 행에 해당하는 n개의 값을 공백을 사이에 두고 출력합니다.
점이 있는 칸은 점의 크기를, 나머지 칸은 0을 출력합합니다.

입출력 예제
입력:
3 3
1 1
3 2
3 3

출력:
1 0 0
0 0 0
0 6 9
"""
n, m = map(int, input().split())

answer = [[0 for _ in range(n)]for _ in range(n)]


for _ in range(m):
    x, y = map(int, input().split())
    answer[x-1][y-1] = x*y

for i in range(n):
    for j in range(n):
        print(answer[i][j], end=" ")
    print()