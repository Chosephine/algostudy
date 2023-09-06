# 백준 11399 ATM
# https://www.acmicpc.net/problem/11399

import sys

input = sys.stdin.readline

# 대기중인 사람 N명,
# 각 사람이 업무 보는데 걸리는 시간의 배열 time
N = int(input().strip())
time = list(map(int, input().strip().split()))

# 시간 소요가 적은 사람부터 업무를 보면 총 대기시간 감소
time.sort()

# 누적합을 위해 순회
for i in range(1, N):
    time[i] += time[i-1]

# 모든 사람이 기다리는 시간의 합
print(sum(time))