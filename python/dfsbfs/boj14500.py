# 백준 14500 테트로미노
# https://www.acmicpc.net/problem/14500

# 시간 재볼라고....
import time
start_time = time.time()

# 19가지 경우의 수 모두 나눠서 코드 짜기 싫어서 머리 굴린 코드
# global 쓰는 거 지양 될텐데, 심지어 갱신까지 해버렸다....

import sys
input = sys.stdin.readline


# 위, 오른쪽, 아래, 왼쪽
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

# check: 재귀적으로 현재블록과 붙어있는 상,우,하,좌 블럭을 탐색하고 합을 계산하는 함수
# [input] cnt: 블럭 갯수 / tetro: 현재의 tetro 에 포함되는 블럭 좌표 / num_sum: 현재 tetro 합계
#         tetro 예시: [(r1, c1), (r2, c2), (r3, c3), (r4, c4)]
# [output] input 한 tetro 의 최대 합
def check(cnt, tetro:list, num_sum: int):
    # 변하지 않을 값 이라서 global 변수 선언
    global N
    global M
    global paper
    global max_block

    # 가지치기 용으로 answer 사용해야해서 global 변수 선언
    global answer

    # 가지치기: max 갱신될 각이 안 나오면 dfs 종료
    if num_sum + (max_block * (4-cnt)) < answer:
        return num_sum

    # 종료조건: block 갯수가 4개라면 answer 갱신 하고 반환
    if cnt == 4:
        answer = max(answer, num_sum)
        return num_sum

    # 일단 tetro들의 합계를 모두 담아 둘 list 생성
    sum_arr = []

    # tetro block 들의 상하좌우를 탐색하여 tetro에 포함되지 않은 블록이면 check 함수 재귀적으로 호출
    for block in tetro:
        cr, cc = block

        # 상하 좌우 탐색
        for d in range(4):
            nr = cr + dx[d]
            nc = cc + dy[d]

            if 0 <= nr < N and 0 <= nc < M and (nr, nc) not in tetro :
                # 재귀를 돌고 현재 블록에서 만들 수 있는 최대 합 받아옴
                temp_sum = check(cnt + 1, tetro + [(nr, nc)], num_sum + paper[nr][nc])
                sum_arr.append(temp_sum)

    # temp_max : 현재의 최대 합
    temp_max = max(sum_arr)

    # 가지치기를 위해 answer 도 갱신 해야 함
    answer = max(answer, temp_max)

    return answer

# N: 행 갯수 / M: 열 갯수
# paper: 각 격자별 점수가 적혀 있는 종이
# max_block: 가지치기를 위해 paper 상 가장 큰 숫자 확인
N, M = map(int, input().split(' '))
paper = [list(map(int, input().split(' '))) for _ in range(N)]
max_block = max(map(max, paper))

answer = 0

# 각 노드별로 dfs 시작
for r in range(N):
    for c in range(M):
        answer = max(answer, check(1, [(r, c)], paper[r][c]))

print(answer)

# 시간 재기용 라인
end_time = time.time()
print('time :', end_time - start_time)