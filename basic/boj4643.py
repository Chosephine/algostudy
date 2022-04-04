# boj4643 셀프 넘버
# https://www.acmicpc.net/problem/4673

def constructor(n):
    start = n

    while start <= 10000:
        con = start
        while start > 0:
            con += start % 10
            start //= 10
        if con <= 10000:
            nums[con] = 1
        start = con



nums = [0 for _ in range(10001)]
for n in range(1, 10001):
    if not nums[n]:
        constructor(n)

for i in range(1, 10001):
    if not nums[i]:
        print(i)
