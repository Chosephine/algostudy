import sys
sys.stdin = open('input.txt')


def minmax(start, pl, mi, mu, di, temp_sum):
    global N, result_max, result_min
    if start == N:
        if temp_sum > result_max:
            result_max = temp_sum
        if temp_sum < result_min:
            result_min = temp_sum
        return
    else:
        if pl > 0:
            minmax(start + 1, pl - 1, mi, mu, di, temp_sum + A[start])
        if mi > 0:
            minmax(start + 1, pl, mi - 1, mu, di, temp_sum - A[start])
        if mu > 0:
            minmax(start + 1, pl, mi, mu - 1, di, temp_sum * A[start])
        if di > 0:
            if temp_sum < 0:
                put_this = - ((- temp_sum) // A[start])
                minmax(start + 1, pl, mi, mu, di - 1, put_this)
            else:
                minmax(start + 1, pl, mi, mu, di - 1, temp_sum // A[start])


N = int(input())
A = list(map(int, input().split()))
# + - x /
O = list(map(int, input().split()))


result_max = - 10 ** 9
result_min = 10 ** 9
sum_start = A[0]
minmax(1, O[0], O[1], O[2], O[3], sum_start)


print(result_max, result_min)