import math, itertools

def aliquot(n):
    arr = set()
    sqtn = int(math.sqrt(n))
    for a in range(1, sqtn + 1):  # aliquot 약수
        if not n % a:
            arr.add(a)
            arr.add(n // a)
    arr = list(arr)
    arr.sort()
    return arr

def gcd(list, n):
    gcd_list = aliquot(list[0])
    for nn in range(1, n):
        n_aliquot = aliquot(n_list[nn])
        new_gcd_list = []
        for m in gcd_list:
            if m in n_aliquot:
                new_gcd_list.append(m)
        gcd_list = new_gcd_list
    return max(gcd_list)

N = int(input())
n_list = list(map(int, input().split()))

gcd = gcd(n_list, N)
print(gcd)

lcm = gcd
lcm_list = [n // gcd for n in n_list]
while True:
    for l in range(max(lcm_list)):


# print(lcm_mat)

