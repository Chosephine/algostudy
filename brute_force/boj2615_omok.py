import sys
sys.stdin = open('1.txt')

arr = [[0] + list(map(int, input().split())) + [0] for _ in range(19)]
arr += [[0] * 21]

def check(stone):
    for r in range(20):
        cnt = 0
        for c in range(21):
            if arr[r][c] == 1:
                cnt += 1
            else:
                if cnt == 5:
                    return r+1, c-5
                cnt = 0
    for c in range(21):
        cnt = 0
        for r in range(20):
            if arr[r][c] == 1:
                cnt += 1
            else:
                if cnt == 5:
                    return r-4, c
                cnt = 0
    r = 0
    cnt = 0
    while r < 20:
        c = 0
        while c<21:
            if arr[r][c] == 1:
                cnt += 1
                r += 1
                c += 1
                if c>20:
                    r -= (cnt-1)
                    break
            else:
                if cnt == 5:
                    return r-4, c-5
                elif cnt > 0:
                    r -= cnt
                    c -= (cnt-1)
                    cnt = 0
                else:
                    c += 1
        r += 1
    r = 0
    cnt = 0
    while r < 20:
        c = 20
        while c>= 0:
            if arr[r][c] == 1:
                r += 1
                c -= 1
                if c < 0:
                    r -= (cnt-1)
                    break
                else:
                    if cnt == 5:
                        return r, c-1
                    r -= cnt
                    c += (cnt-1)
                    cnt = 0
        r += 1


if check(1):
    print('1')
    print(*check(1))
elif check(2):
    print('2')
    print(*check(2))
else:
    print('0')

