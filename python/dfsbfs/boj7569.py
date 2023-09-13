import sys
from collections import deque

input=sys.stdin.readline

# return 을 통해 함수 종료시키기 위해 함수 정의
def solution(original, H, N, M):

    # 델타
    # dh: 층 이동(위층, 아래층) / dn: 세로 이동(위, 아래) / dm: 가로 이동(왼, 오)
    dh = (1, -1, 0, 0, 0, 0)
    dn = (0, 0, -1, 0, 1, 0)
    dm = (0, 0, 0, 1, 0, -1)

    # bfs를 위한 q 초기화
    # riped_tomato : 익은 토마토 개수
    q = deque()
    riped_tomato = 0
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if original[h][n][m] == 1:
                    # ==== 처음 코드가 메모리 초과였기 때문에 공간 복잡도를 줄이기 위해 day 를 큐에 넣지 않기로 함 ====
                    # q.append((h, n, m, 1))
                    # ============================================================================
                    riped_tomato += 1
                    q.append((h, n, m))

    # 토마토 갯수가 박스 칸 갯수와 동일하다면 0 반환
    if riped_tomato == H * N * M:
        return 0

    # 최장 기간을 순환하지 않기 위해 max_day 변수 설정
    max_day = 0
    while q:
        # q 순서 대로 꺼내서 6방향 탐색
        ch, cn, cm = q.popleft()
        day = original[ch][cn][cm]

        # max_day 갱신
        if day > max_day:
            max_day = day

        for d in range(6):
            nh = ch + dh[d]
            nn = cn + dn[d]
            nm = cm + dm[d]
            if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M and not original[nh][nn][nm]:
                # ==== 처음 코드가 메모리 초과였기 때문에 공간 복잡도를 줄이기 위해 day 를 큐에 넣지 않기로 함 ====
                # print((nh, nn, nm, day+1))
                # ============================================================================
                original[nh][nn][nm] = day + 1
                q.append((nh, nn, nm))

    # 익지 않은 토마토 있으면 -1 반환
    for vh in range(H):
        for vn in range(N):
            for vm in range(M):
                if original[vh][vn][vm] == 0:
                    return -1

    # 위에서 리턴되지 않았다면, 모두 익는데 소요된 시간 반환
    return max_day - 1


# M: 가로 / N: 세로 / H: 층
M, N, H = map(int, input().split())

# tomato_boxes: 토마토 현황
tomato_boxes = []

# h 층에 있는 토마토 현황을
# stair 이라는 2차원 배열에 담기
for h in range(H):
    stair = []
    for n in range(N):
        m = list(map(int, input().split()))
        stair.append(m)
    tomato_boxes.append(stair)


print(solution(tomato_boxes, H, N, M))