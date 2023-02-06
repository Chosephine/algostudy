import itertools
import sys
sys.stdin = open('input.txt')

vowels = ['a', 'e', 'i', 'o', 'u']

L, C = map(int, input().split())
candidates = list(input().split())
comb = list(itertools.combinations(candidates, L))
# comb.sort()
result = []
for t in comb:
    cnt_v = 0
    cnt_nv = 0
    # print(t)
    for i in range(L):
        if t[i] in vowels:
            cnt_v += 1
        else:
            cnt_nv += 1
        # print(cnt_v, cnt_nv)
        if cnt_v >= 1 and cnt_nv >= 2:
            break
    else:
        continue
    codes = list(map(ord, t))
    codes.sort()
    password = list(map(chr, codes))
    result.append(''.join(password))
result.sort()
for i in result:
    print(i)