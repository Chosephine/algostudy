import sys
sys.stdin = open('input.txt')


def paper(arr, N):
    global cnt0
    global cnt1
    # 기저부
    first = arr[0][0]
    ifbreak = 0
    for r in range(N):
        for c in range(N):
            if first != arr[r][c]:
                ifbreak = 1
                break
        if ifbreak:
            break
    else:
        if first:
            cnt1 += 1
            return
        else:
            cnt0 += 1
            return
    # 실행부
    NN = N // 2
    narr = [[_ for _ in range(NN)] for _ in range(NN)]
    # 2사분면
    for r in range(NN):
        for c in range(NN):
            narr[r][c] = arr[r][c]
    paper(narr, NN)
    # 1사분면
    for r in range(NN):
        for c in range(NN, N):
            narr[r][c-NN] = arr[r][c]
    paper(narr, NN)
    # 3사분면
    for r in range(NN, N):
        for c in range(NN):
            narr[r-NN][c] = arr[r][c]
    paper(narr, NN)
    # 4사분면
    for r in range(NN, N):
        for c in range(NN, N):
            narr[r-NN][c-NN] = arr[r][c]
    paper(narr, NN)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt0 = 0
cnt1 = 0

paper(arr, N)

print(cnt0)
print(cnt1)




