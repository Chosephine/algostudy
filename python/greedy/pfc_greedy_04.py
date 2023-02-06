from itertools import combinations

# N = 5
# coins = [3, 2, 1, 1, 9]

N = 3
coins = [3, 5, 7]


coins.sort()  # [1, 1, 2, 3, 9]

max_coin = coins[-1]
memo = [0] * (max_coin * N + 1)
memo[0] = 1

for i in range(max_coin):
    combs = combinations(coins, i)
    for c in combs:
        memo[sum(c)] = 1

for j in range(len(memo)):
    if not memo[j]:
        print(j)
        break


