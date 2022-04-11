# boj7568 덩치
# https://www.acmicpc.net/problem/7568


def solve(turn, x, y):
    global rates
    if turn == 0:
        rates[turn] = [turn + 1, x, y]
    else:
        cnt_big = 0
        for p in range(turn):
            if rates[p][1] < x and rates[p][2] < y:  # 덩치 큼
                rates[turn] = [rates[p][0], x, y]
                rates[p][0] += 1
            elif rates[p][1] > x and rates[p][2] > y:  # 덩치 작음
                rates[turn] = [rates[p][0] + 1, x, y]
                cnt_big += 1
            else:  # 비등비등
                rates[turn] = [rates[p][0], x, y]
        rates[turn] = [cnt_big + 1, x, y]


N = int(input())
rates = [0] * N
for i in range(N):
    w, h = map(int, input().split())
    solve(i, w, h)

for j in range(N):
    print(rates[j][0], end=' ')

