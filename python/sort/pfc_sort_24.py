# https://www.acmicpc.net/problem/18310
# 이코테 기출 24, 백준 18310

N = int(input())
houses = list(map(int, input().split()))
houses.sort()
# print(houses)
# houses_distance = [0] * N

min_idx = N + 1
min_dst = 100000 * 200000
for i in range(N):
    antenna = houses[i]
    distance = 0
    for house in houses:
        distance += abs(house - antenna)
        if distance > min_dst:
            break
    # houses_distance[i] = distance
    if distance < min_dst:
        min_idx = i
        min_dst = distance

print(houses[min_idx])

# 시간초과....
# 떠오른 간단한 그거 맞아..^^...