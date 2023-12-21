# 백준 11403 경로 찾기
# https://www.acmicpc.net/problem/11403


if __name__ == "__main__":
    import sys
    from collections import deque

    input = sys.stdin.readline

    N = int(input())
    G = [list(map(int, input().split())) for _ in range(N)]

    result = [[-1] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):

            s = deque()
            s.append(i)
            used = [0] * N
            flag = True

            while s:
                target = s.popleft()

                if target == j and not flag:
                    result[i][j] = 1
                    break
                else:
                    flag = False


                if result[target][j] > 0:
                    result[i][j] = 1
                    break
                elif result[target][j] < 0:
                    for k in range(N):
                        if G[target][k] > 0 and not used[k]:
                            result[target][k] = 1
                            s.append(k)
                            used[k] = 1

            if result[i][j] < 0 and len(s) == 0:
                result[i][j] = 0

    for i in range(N):
        for j in range(N-1):
            print(result[i][j], end=' ')
        print(result[i][N-1])