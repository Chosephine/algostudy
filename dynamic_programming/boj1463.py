# boj1463 1로 만들기
# https://www.acmicpc.net/problem/1463

N = int(input())


# dp.. 원앤온리......
memo = [0] * (N+1)

for i in range(2, N+1):
    memo[i] = memo[i-1] + 1
    if not i % 3:
        memo[i] = min(memo[i], memo[i // 3] + 1)
    if not i % 2:
        memo[i] = min(memo[i], memo[i // 2] + 1)

print(memo[N])


# 시간초과ㅠ

# result = 10 ** 6
# def operation(n, count):
#     global result
#     if count > result:
#         return
#     if n == 1:
#         if result > count:
#             result = count
#         return
#     else:
#         if not n % 3:
#             operation(n//3, count+1)
#         if not n % 2:
#             operation(n//2, count+1)
#         operation(n-1, count+1)
#
#
# operation(N, 0)
# print(result)

'''

count = 0
while True:
    if N == 1:
        if count < result:
            result = count
        break
    else:
        if not N % 3:
            N //= 3
            count += 1
        if not N % 2:
            N //= 2
            count += 1
        N -= 1
        count += 1


'''












