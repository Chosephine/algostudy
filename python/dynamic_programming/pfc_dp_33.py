# 이코테 기출 33 퇴사
# https://www.acmicpc.net/problem/14501

import sys

# T: i일에 잡혀 있는 상담 소요일 / P: i일에 잡혀 있는 상담 비용 / N: 상담 가능 기간
T = [0]
P = [0]
N = int(sys.stdin.readline())
for _ in range(N):
    t, p = map(int, sys.stdin.readline().split())
    T.append(t)
    P.append(p)

# I: 수입 / idx 1 ~ N가 상담일, N+1은 퇴사일
I = [0] * (N+2)

# N 일부터 역산
for n in range(N, 0, -1):
    # n일의 T, P
    t, p = T[n], P[n]

    if n + t > N + 1:사

    I[n] = max( I[n + 1], I[n + t] + P[n] )


print(I[1])