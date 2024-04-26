def solution(board, moves):
    answer = 0
    stack = []
    basket = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] == 0:
                continue
            basket.append(board[j][i - 1])
            board[j][i - 1] = 0
            break

    for i in range(len(basket)):
        if stack and basket[i] == stack[-1]:
            stack.pop()
            answer += 2
        else:
            stack.append(basket[i])
    return answer