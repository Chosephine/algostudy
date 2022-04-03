# boj10162 전자렌지
# https://www.acmicpc.net/problem/10162

T = int(input())
a = b = c = 0

# 1. 일일이 돌린다
# if T % 10:
#     print(-1)
# else:
#     while T > 0:
#         if T >= 300:
#             a += 1
#             T -= 300
#         elif T >= 60:
#             b += 1
#             T -= 60
#         else:
#             c += 1
#             T -= 10
#     print(a, b, c)

# -----------------------------

# 2. 쫌 머리를 써서 일일이 돌린다
#
# if T % 10:
#     print(-1)
# else:
#     while T > 0:
#         if T >= 300:
#             a += T // 300
#             T -= 300 * a
#         elif T >= 60:
#             b += T // 60
#             T -= 60 * b
#         else:
#             c += T // 10
#             T -= 10 * c
#     print(a, b, c)

# ----------------------------

if T % 10:
    print(-1)
else:
    if T >= 300:
        a = T // 300
        T -= 300 * a
        a = str(a)
    if T >= 60:
        b = T // 60
        T -= 60 * b
    if T >= 10:
        c = T // 10
    print(a, b, c)

