import math
N = int(input())
arr = set()
sqtN = int(math.sqrt(N))

for a in range(1, sqtN + 1):  # aliquot 약수
    if not N % a:
        arr.add(a)
        arr.add(N // a)

# print(memo)
arr = list(arr)
arr.sort()
print(*arr)

