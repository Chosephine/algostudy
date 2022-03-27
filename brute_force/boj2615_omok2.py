import sys
sys.stdin = open('2.txt')

arr = [list(map(int, input().split())) for _ in range(19)]

def check(stone):
    cnt = 0
    for r in range(19):
        for c in range(19):
            if arr[r][c] == stone:
                cnt += 1
                if c == 18 and cnt == 5:
                    return 'row', r, c - cnt + 1
            else:
                if cnt == 5:
                    return 'row', r, c - cnt + 1
                cnt = 0


    cnt = 0
    for c in range(19):
        for r in range(19):
            if arr[r][c] == stone:
                cnt += 1
                if r == 18 and cnt == 5:
                    return 'col', r, c - cnt + 1
            else:
                if cnt == 5:
                    return 'col', r, c - cnt + 1
                cnt = 0

    r = 0
    while r < 19:
        cnt_d = 0
        c = 0
        while c < 19:
            if arr[r][c] == stone:
                if cnt_d == 4 and c ==18:
                    return 'diag1', r - cnt_d, c - cnt_d
                if c == 18 and cnt_d < 4:
                    r = r - cnt_d + 1
                    c = 0
                    cnt_d = 0
                r += 1
                c += 1
                cnt_d += 1
                continue
            else:
                if cnt_d == 5:
                    return 'diag1', r - cnt_d, c - cnt_d + 1
                c = c - cnt_d + 1
                r -= cnt_d
                cnt_d = 0
        r += 1

    r = 0
    while r < 19:
        cnt_d = 0
        c = 18
        while c > -1:
            if arr[r][c] == stone:
                if cnt_d == 4 and c ==0:
                    return 'diag2', r, c
                if c == 0 and cnt_d < 4:
                    r = r - cnt_d + 1
                    c = 18
                    cnt_d = 0
                r += 1
                c -= 1
                cnt_d += 1
                continue
            else:
                if cnt_d == 5:
                    return 'diag2', r - 1, c + 1
                c = c + cnt_d - 1
                r -= cnt_d
                cnt_d = 0
        r += 1

    return

if check(1) and check(2):
    print('0')
elif check(1):
    print('1')
    print(*check(1))
elif check(2):
    print('2')
    print(*check(2))
else:
    print('0')

