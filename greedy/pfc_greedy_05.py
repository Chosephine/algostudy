N, M = map(int, input().split())
arr = list(map(int, input().split()))

num_cnt = [0] * (M + 1)
over2 = 0
for a in arr:
    num_cnt[a] += 1
    if num_cnt[a] == 2:
        over2 += 1

result = ((N * (N - 1)) / 2) - over2

print(int(result))