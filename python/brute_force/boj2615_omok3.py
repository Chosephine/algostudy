import sys
sys.stdin = open('2.txt')

arr = [[0] * 21] + [[0] + list(map(int, input().split())) + [0] for _ in range(19)] + [[0] * 21]


def check(stone):
    for r in range(21):
        cnt = 0
        for c in range(21):
            if arr[r][c] == stone:
                cnt += 1
            else:
                if cnt == 5:
                    return 'row', r, c-5
                cnt = 0
    for c in range(21):
        cnt = 0
        for r in range(21):
            if arr[r][c] == stone:
                cnt += 1
            else:
                if cnt == 5:
                    return 'col', r-5, c
                cnt = 0
    r = 0
    cnt = 0
    while r < 21:
        c = 0
        while c < 21:
            if arr[r][c] == stone:
                cnt += 1
                r += 1
                c += 1
            else:
                if cnt == 5:
                    return 'diag1', r-5, c-5
                elif cnt > 0:
                    r -= cnt
                    c -= (cnt-1)
                    cnt = 0
                else:
                    c += 1
        r += 1

    r = 0
    cnt = 0
    while r < 21:
        c = 20
        while c >= 0:
            if arr[r][c] == stone:
                cnt += 1
                r += 1
                c -= 1
            else:
                if cnt == 5:
                    return 'diag2', r-1, c+1
                elif cnt > 0:
                    r -= cnt
                    c += (cnt-1)
                    cnt = 0
                else:
                    c -= 1
        r += 1


if check(1):
    print('1')
    print(*check(1))
elif check(2):
    print('2')
    print(*check(2))
else:
    print('0')

# print(arr)