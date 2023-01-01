# boj 2022 송년대회 A 시로코와 은행털기

n, k, x = map(int, input().split())
people = [] * n
for _ in range(n):
    people.append(tuple(map(int, input().split())))


max_ability = 0

def pick(i, j, sum_a, sum_b): # 이전에 뽑힌 사람 idx는 i, j번째 사람 pick
    global max_ability, result_set, k
    if j >= k:
        ability = sum_a * sum_b
        if max_ability < ability:
            max_ability = ability
            print(sum_a, sum_b)
        return
    for l in range(i, n):
        pick(l, j + 1, sum_a+people[l][0], sum_b+people[l][1])

for m in range(n):
    pick(m, 1, people[m][0], people[m][1])

# print(type(people[0][1]))
print(max_ability)