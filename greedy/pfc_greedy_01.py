# N = 5
N = 3
# adventurers = [2, 3, 1, 2, 2]
adventurers = [1, 1, 1]  # 5 2 2 2 1 1 1
adventurers.sort(reverse=True)
# print(adventurers)
group = 0
current = 0
c_max = adventurers[current]
for i in range(N):
    if adventurers[i] <= c_max:
        current += 1
        if current == c_max and i < N - 1:
            group += 1
            current = 0
            c_max = adventurers[i + 1]
if current > 0:
    group += 1
print(group)
