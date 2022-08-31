# https://www.acmicpc.net/problem/3190
# 이코테 파이썬 기출 11, 백준 '뱀'

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# N: 보드의 크기, K: 사과의 개수, L: 방향 변환 횟수
N = int(input())
K = int(input())
apples_position = [list(map(int, input().split())) for _ in range(K)]  # 좌표 (1, 1)부터 시작
L = int(input())
turn = [list(input().split()) for _ in range(L)]  # ['3','L'] 꼴

board = [[0] * (N + 2) for _ in range(N + 2)]  # 좌표 (0, *), (* , 0) 은 안 쓰는 거야

for apple in apples_position:
    board[apple[0]][apple[1]] = 1

# snake 위치 초기화 (idx=0이 머리)
current_snake = [(1, 2), (1, 1)]
# timer: 시간, turn_idx: 회전 차례, d: 델타 idx
timer = turn_idx = d = 0

while True:
    timer += 1
    # 뱀 몸 늘리기 or 이동
    sr, sc = current_snake[0]
    if board[sr][sc]:
        board[sr][sc] = 0
        sr += dr[d]
        sc += dc[d]
        new_snake = [(sr, sc)] + current_snake
    else:
        sr += dr[d]
        sc += dc[d]
        new_snake = [(sr, sc)] + current_snake[:-1]

    if turn_idx < L and str(timer) == turn[turn_idx][0]:
        # 회전하기
        if turn[turn_idx][1] == 'D':
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4
        turn_idx += 1

    current_snake = new_snake

    # 벽 또는 몸인지 확인
    if new_snake[0] in new_snake[1:len(new_snake)]:
        break
    elif new_snake[0][0] == N + 1 and d == 1:
        break
    elif new_snake[0][0] == 1 and d == 3:
        break
    elif new_snake[0][1] == N + 1 and d == 0:
        break
    elif new_snake[0][1] == 1 and d == 2:
        break


print(timer)



