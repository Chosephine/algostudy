import sys
sys.stdin = open('input.txt')

a = input()
b = input()
str1 = str2 = None
N = M = 0
if len(a) < len(b):
    str1, str2 = a, b
    N = len(a)
    M = len(a)
else:
    str1, str2 = b, a
    N = len(b)
    M = len(a)

bit = [0] * N
max_len = 0


def check(str_s, n, str_l, m):
    global max_len
    s = -1
    cnt = 0
    for k in bit:
        cnt += k

    if cnt <= max_len:
        return

    for i in range(n):
        if bit[i] == 1:
            for j in range(s+1, m):
                if str_l[j] == str_s[i]:
                    s = j
                    break
            else:
                return
    else:
        max_len = cnt
        return


def powerset(k, stop):
    bit[k] = 1
    if k == stop - 1:
        check(str1, N, str2, M)
        bit[k] = 0
        check(str1, N, str2, M)
        return
    else:
        k += 1
        powerset(k, stop)
        bit[k-1] = 0
        powerset(k, stop)


powerset(0, N)
print(max_len)
