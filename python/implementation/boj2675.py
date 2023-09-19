# 백준 2675 문자열 반복
# https://www.acmicpc.net/problem/2675

T = int(input())

for _ in range(T):
    R, P = input().split(' ')
    R = int(R)

    answer = ''
    for p in P:
        answer += p * R

    print(answer)