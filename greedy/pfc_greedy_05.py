N, M = map(int, input().split())
arr = list(map(int, input().split()))

num_cnt = [0] * (M + 1)

for a in arr:
    num_cnt[a] += 1

over2 = 0
for i in range(len(num_cnt)):
    n = num_cnt[i]
    if n >= 2:
        over2 += ((n * (n - 1)) / 2)


result = ((N * (N - 1)) / 2) - over2

print(int(result))