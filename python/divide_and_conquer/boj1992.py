import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(input() for _ in range(N))


def is_same(array, size):
    s = array[0][0]
    for r in range(size):
        for c in range(size):
            if s != array[r][c]:
                return False
    else:
        return True

# nn = N//2
# narr = [[0]*nn for _ in range(nn)]
# # 2사분면
# for r in range(nn):
#     for c in range(nn, N):
#         narr[r][c-nn] = arr[r][c]
# print(narr, '\n', is_same(narr, nn))


def qt(array, n):
    global result
    if is_same(array, n):
        result += str(array[0][0])
        return
    else:
        result += '('
        nn = n//2
        narr = [[0]*nn for _ in range(nn)]
        # 1사분면
        for r in range(nn):
            for c in range(nn):
                narr[r][c] = array[r][c]
        qt(narr, nn)
        # 2사분면
        for r in range(nn):
            for c in range(nn, n):
                narr[r][c-nn] = array[r][c]
        qt(narr, nn)
        # 4사분면
        for r in range(nn, n):
            for c in range(nn):
                narr[r-nn][c] = array[r][c]
        qt(narr, nn)
        # 3사분면
        for r in range(nn, n):
            for c in range(nn, n):
                narr[r-nn][c-nn] = array[r][c]
        qt(narr, nn)
        result += ')'


result = ''
qt(arr, N)


print(result)