import sys
sys.stdin = open('sample_input.txt')


def check1(arr, n):
    for i in range(n):
        cnt_r = 0
        cnt_c = 0
        for j in range(n):
            if arr[i][j] == 'o':
                cnt_r += 1
            if arr[j][i] == 'o':
                cnt_c += 1
        if cnt_r >= 5 or cnt_c >= 5:
            return True
    return False


def check2(arr, n):
    for r in range(n-4):
        for c in range(n-4):
            cnt = 0
            for i in range(5):
                if arr[r+i][c+i] == 'o':
                    cnt += 1
                else:
                    break
            if cnt >= 5:
                return True
    return False


def check3(arr, n):
    for r in range(n-4):
        for c in range(n-1, 3, -1):
            cnt = 0
            for i in range(5):
                if arr[r+i][c-i] == 'o':
                    cnt += 1
                else:
                    break
            if cnt >= 5:
                return True
    return False


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    omok = [input() for _ in range(N)]
    rc = check1(omok, N)
    dia1 = check2(omok, N)
    dia2 = check3(omok, N)

    if rc or dia1 or dia2:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')
