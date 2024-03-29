"""
최고의 33위치

N * N 크기의 격자 정보가 주어집니다. 이때 해당 위치에 동전이 있다면 1, 없다면 0이 주어집니다. N * N 격자를 벗어나지 않도록 3 * 3 크기의 격자를 적절하게 잘 잡아서 해당 범위 안에 들어있는 동전의 개수를 최대로 하는 프로그램을 작성해보세요.

입력 형식
첫 번째 줄에는 격자의 크기를 나타내는 N이 주어집니다.
두 번째 줄부터는 N개의 줄에 걸쳐 격자에 대한 정보가 주어집니다. 각 줄에는 각각의 행에 대한 정보가 주어지며, 이 정보는 0또는 1로 이루어진 N개의 숫자로 나타내어지며 공백을 사이에 두고 주어집니다.
3 ≤ N ≤ 20

출력 형식
N * N 격자를 벗어나지 않으면서, 3 * 3 크기 격자 내에 들어올 수 있는 최대 동전의 수를 출력해주세요.

입출력 예제
입력:
3
1 0 1
0 1 0
0 1 0

출력:
4
"""
n = int(input())

answer = []
for i in range(n):
    answer.append(list(map(int, input().split())))

count = 0
for i in range(n):
    temp = 0
    if i + 2 >= n:
        continue
    for j in range(n):
        if j + 2 >= n:
            continue
        temp = answer[i][j] + answer[i+1][j] + answer[i+2][j] + answer[i][j+1] + answer[i][j+2] + answer[i+1][j+1]+ answer[i+1][j+2]+ answer[i+2][j+1]+ answer[i+2][j+2]
        if temp >= count:
            count = temp

print(count)