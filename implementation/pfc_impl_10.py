def rotateKey(key):
    target = key
    M = len(target)
    keys = []
    for cycle in range(3):
        newkey = [[0] * M for _ in range(M)]
        for r in range(M):
            for c in range(M):
                newkey[M-1-c][r] = target[r][c]
        keys.append(newkey)
        target = newkey
    return keys


def check(key, lock):
    N = len(lock)
    M = len(key)
    newlock = [[0] * (N + (M - 1) * 2) for _ in range(N)]
    for r in range(N):
        for c in range(N):
            newlock[r + (M-1)][c + (M-1)] = lock[r][c]

    for i in range(N + M - 1):
        for j in range(N + M - 1):
            for rr in range(M):
                for cc in range(M):
                    newlock[i + rr][j + cc] += key[rr][cc]
            for rr in range(M-1, N + M - 1):
                for cc in range(M-1, N + M - 1):
                    if newlock[rr][cc] != 1:
                        for rr in range(M):
                            for cc in range(M):
                                newlock[i + rr][j + cc] -= key[rr][cc]



def solution(key, lock):
    keyset = [key]
    keyset += rotateKey(key)
    # print(keyset)
    for i in range(4):
        if check(keyset[i], lock):
            return true
    return false

solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],  [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
