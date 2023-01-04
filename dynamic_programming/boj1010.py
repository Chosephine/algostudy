# boj1010 다리놓기
# https://www.acmicpc.net/problem/1010

# T = int(input())
# for t in range(T):
#     N, M = map(int, input().split())
#     s = M
#     son = 1
#     mother = 1
#     while s >= (M - N + 1):
#         son *= s
#         s -= 1
#     for m in range(1, N + 1):
#         mother *= m
#     print(son//mother)

# ==================== ver. dp =======================

fact = [1] * 31
for i in range(1, 31):
    fact[i] = fact[i-1] * i
# print(fact)

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    son = fact[M]
    mother = fact[N] * fact[M-N]
    print(son//mother)