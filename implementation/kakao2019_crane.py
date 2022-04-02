def solution(board, moves):
    # board idx 0~N-1
    # moves idx 1~N -> -1씩 해주기
    N = len(board)
    basket = []
    cnt = 0
    for move in moves:
        doll_idx = -1
        # 이번 turn에서 제일 상위에 있는 인형 위치 확인
        for stair in range(N):
            if board[stair][move - 1]:
                doll_idx = stair
                break
        else:  # break 안 걸리면 다음 move로
            continue

        # 인형 basket에 담기
        if basket and basket[-1] == board[doll_idx][move - 1]:
            basket.pop()
            board[doll_idx][move - 1] = 0
            cnt += 2
        else:
            basket.append(board[doll_idx][move - 1])
            board[doll_idx][move - 1] = 0

    answer = cnt
    return answer