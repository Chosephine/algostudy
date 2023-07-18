# 이코테 기출 36 편집 거리
# Goldman Sachs 인터뷰

import sys

input = sys.stdin.readline

# A to B, 1 <= len(A), len(B) <= 5000
A = input().strip()
B = input().strip()

# A와 B를 순회하면서 동일한 알파벳을 찾는 배열 생성
indices = []

# 시간복잡도 최대 5000 * 5000
for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            indices.append(j)

# 최장 증가 수열 길이를 담을 dp
dp = [0] * len(indices)

for i in range(len(indices)):
    for j in range(i):
        if indices[i] > indices[j]:
            dp[i] = max(dp[j], dp[i] + 1)

# 둘 중 더 긴 문자열 길이에서 최장증가수열 길이를 빼면 필요한 연산 횟수
print(max(len(A), len(B)) - max(dp))
