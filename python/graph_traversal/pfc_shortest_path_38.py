# 이코테 기출 38 정확한 순위

import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

grades = [[INF] * n for _ in range(n)]

# 자기 비교는 0
for i in range(n):
    for j in range(n):
        if i == j:
            grades[i][j] = 0

# 비교 데이터 넣기 : grades[a][b]이 1이라면 a가 b보다 작음을 뜻한다
for _ in range(m):
    small, big = map(int, input().split())
    grades[small - 1][big - 1] = 1

# Floyd warshall
for k in range(n):
    for a in range(n):
        for b in range(n):
            grades[a][b] = min(grades[a][b], grades[a][k] + grades[k][b])

# i와 j가 비교 가능하다면 INF가 아닌 값이 있을 것이고,
# 모든 노드들과 비교가능하다면 해당 숫자의 순위를 알 수 있다는 것
answer = 0

for i in range(n):
    cnt = 0
    for j in range(n):
        if grades[i][j] != INF or grades[j][i] != INF:
            cnt += 1
    if cnt == n:
        answer += 1

print(answer)