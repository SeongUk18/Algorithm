def is_safe(board, row, col, N):
    # 같은 열에 다른 퀸이 있는지 확인
    for i in range(row):
        if board[i][col] == 1:
            return False

    # 왼쪽 상단 대각선에 다른 퀸이 있는지 확인
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    # 오른쪽 상단 대각선에 다른 퀸이 있는지 확인
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, row, N):
    # 모든 퀸을 배치했다면 해결책을 찾은 것
    if row == N:
        for r in board:
            print(r)
        print("\n")
        return

    # 각 행에서 모든 열에 퀸을 놓아보기
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1  # 퀸을 배치
            solve_n_queens(board, row + 1, N)  # 다음 행으로 이동
            board[row][col] = 0  # 백트래킹 (이 열에 퀸을 놓는 방법을 포기)


# N-Queen 문제 해결 (4-Queen 예시)
N = 4
board = [[0] * N for _ in range(N)]
solve_n_queens(board, 0, N)
