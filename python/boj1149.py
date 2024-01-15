# 백준 1149 RGB거리
# https://www.acmicpc.net/problem/1149


if __name__ == "__main__":
    import sys

    input = sys.stdin.readline

    N = int(input())

    # former_color_info 에서 각 숫자가 의미하는 것
    # 0 : R / 1 : G / 2 : B
    former_color_info = None
    min_cost = 0

    for _ in range(N):
        costs = list(map(int, input().split()))
        for i in range(3):
            costs[i] = (costs[i], i)

        costs.sort()

        if costs[0][1] != former_color_info:
            min_cost += costs[0][0]
            former_color_info = costs[0][1]
            print(costs[0][0])
        else:
            min_cost += costs[1][0]
            former_color_info = costs[1][1]
            print(costs[1][0])

    print(min_cost)