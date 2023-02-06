def solution(m, n, board):
    test_board = [[_ for _ in board[i]] for i in range(m)]
    answer = 0
    while True:
        disapear = [[0] * n for _ in range(m)]
        for r in range(m - 1):
            for c in range(n - 1):
                if test_board[r][c] and test_board[r][c] == test_board[r][c + 1]:
                    for k in range(1, m - r):
                        if not disapear[r+k][c]:

                        if test_board[r][c] == test_board[r + k][c] and test_board[r][c] == test_board[r + k][c + 1]:
                            disapear[r][c] = 1
                            disapear[r][c + 1] = 1
                            disapear[r + k][c] = 1
                            disapear[r + k][c+1] = 1
                            break

        disapear_cnt = 0
        for row in disapear:
            disapear_cnt += sum(row)
        answer += disapear_cnt
        if not disapear_cnt:
            break
        else:
            for c in range(n):
                for r in range(m-1):
                    if not disapear[r][c] and disapear[r+1][c]:
                        test_board[r+1][c] = test_board[r][c]
                        test_board[r][c] = 0
                        disapear[r+1][c] = 0
                    if disapear[r][c] and disapear[r+c][c]:
                        test_board[r + 1][c] = 0
                        test_board[r][c] = 0
        cnt = 1
    return answer


print(solution(7, 2, ["AA", "BB", "AA", "BB", "ZZ", "ZZ", "CC"]))