# boj1463 1로 만들기
N = int(input())
result = 10 ** 6


def operation(n, count):
    global result
    if count > result:
        return
    if n == 1:
        if result > count:
            result = count
        return
    else:
        if not N % 3:
            operation(n//3, count+1)
        if not N % 2:
            operation(n//2, count+1)
        operation(n-1, count+1)


operation(N, 0)

'''

count = 0
while True:
    if N == 1:
        if count < result:
            result = count
        break
    else:
        if not N % 3:
            N //= 3
            count += 1
        if not N % 2:
            N //= 2
            count += 1
        N -= 1
        count += 1
'''
print(result)
