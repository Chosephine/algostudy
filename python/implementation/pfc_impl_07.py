# https://www.acmicpc.net/problem/18406
# 10분! 컷!

def cal_part(str):
    target = int(str)
    result = 0
    while target >= 1:
        result += target % 10
        target //= 10
    return result


N = input()
len_N = len(N)
len_part = len_N // 2
n1 = N[0:len_part]
n2 = N[len_part:]

if cal_part(n1) == cal_part(n2):
    print('LUCKY')
else:
    print('READY')
